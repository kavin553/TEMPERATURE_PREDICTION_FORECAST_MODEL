# train_xgb_combined.py
"""
Load two CSVs, combine, preprocess, create features, train XGBoost, save model + feature list.
Adjust file names / column mappings below if your files are different.
"""
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics import mean_absolute_error
import xgboost as xgb
import os

# --- CONFIG --- #
FILES = [
    {"path": "MLTempDataset1.csv", "time_col": "Datetime", "temp_col": "Hourly_Temp", "source": "A"},
    {"path": "MLTempDataset.csv",  "time_col": "Datetime", "temp_col": "DAYTON_MW",  "source": "B"},
]
OUTPUT_MODEL = "xgb_model_combined.joblib"
OUTPUT_FEATURES = "feature_info_combined.joblib"

# Forecast settings
HORIZON = 1          # predict 1 step ahead (1 hour ahead if data is hourly)
LAGS = [1,2,3,6,12]  # in number of readings (for hourly data these are hours)
TEST_FRACTION = 0.2

# --- 1) LOAD & NORMALIZE --- #
dfs = []
for f in FILES:
    if not os.path.exists(f["path"]):
        raise FileNotFoundError(f"File not found: {f['path']}")
    df = pd.read_csv(f["path"])
    # pick time & temp columns, rename them
    if f["time_col"] not in df.columns or f["temp_col"] not in df.columns:
        raise ValueError(f"Expected columns {f['time_col']} and {f['temp_col']} in {f['path']}. Found: {df.columns.tolist()}")
    df = df[[f["time_col"], f["temp_col"]]].copy()
    df = df.rename(columns={f["time_col"]: "timestamp", f["temp_col"]: "temp"})
    df["source"] = f["source"]
    # parse datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    dfs.append(df)

# Concatenate
df_all = pd.concat(dfs, ignore_index=True)

# --- 2) AGGREGATE / ALIGN --- #
# Set to hourly frequency by grouping on timestamp (if there are duplicate timestamps from sources)
# We'll average temps across sources for same timestamp (you could also keep them separate)
df_all = df_all.groupby("timestamp", as_index=False).agg({"temp": "mean"})
df_all = df_all.sort_values("timestamp").reset_index(drop=True)

# OPTIONAL: resample to hourly (unify frequency). If your data is already hourly this is ok.
# use lowercase 'h' to avoid FutureWarning in newer pandas
df_all = df_all.set_index("timestamp").resample("h").mean()

# Fill small gaps (forward/backward fill)
df_all["temp"] = df_all["temp"].ffill().bfill()

df_all = df_all.reset_index()
print(f"Combined data range: {df_all['timestamp'].min()} -> {df_all['timestamp'].max()}, rows: {len(df_all)}")

# --- 3) FEATURE ENGINEERING --- #
def create_features(df, lags=LAGS):
    df = df.copy()
    df["hour"] = df["timestamp"].dt.hour
    df["day"] = df["timestamp"].dt.day
    df["weekday"] = df["timestamp"].dt.weekday
    for lag in lags:
        df[f"lag_{lag}"] = df["temp"].shift(lag)
    # rolling statistics (with shift to avoid leakage)
    df["roll_mean_6"] = df["temp"].rolling(window=6).mean().shift(1)
    df["roll_std_6"]  = df["temp"].rolling(window=6).std().shift(1)
    df["roll_mean_24"] = df["temp"].rolling(window=24).mean().shift(1)
    return df

df_feat = create_features(df_all)
df_feat["target"] = df_feat["temp"].shift(-HORIZON)
df_feat = df_feat.dropna().reset_index(drop=True)

# List of features used for training
exclude = ["timestamp", "temp", "target"]
features = [c for c in df_feat.columns if c not in exclude]
print("Features used:", features)

# --- 4) TRAIN / TEST SPLIT (time-based) --- #
split_idx = int((1 - TEST_FRACTION) * len(df_feat))
train = df_feat.iloc[:split_idx]
test  = df_feat.iloc[split_idx:]

X_train, y_train = train[features], train["target"]
X_test, y_test   = test[features], test["target"]

# --- 5) TRAIN XGBoost --- #
model = xgb.XGBRegressor(
    n_estimators=400,
    learning_rate=0.05,
    max_depth=6,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42
)
# Fit model. Some xgboost versions accept `early_stopping_rounds` in the sklearn API,
# others do not. Try with early stopping and fall back to a simple fit if unsupported.
try:
    model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        early_stopping_rounds=20,
        verbose=True
    )
except TypeError:
    print("Note: `early_stopping_rounds` not supported by this xgboost version; fitting without early stopping.")
    model.fit(
        X_train, y_train,
        eval_set=[(X_test, y_test)],
        verbose=True
    )

preds = model.predict(X_test)
mae = mean_absolute_error(y_test, preds)
print(f"Test MAE: {mae:.4f}")

# --- 6) SAVE --- #
joblib.dump(model, OUTPUT_MODEL)
joblib.dump(features, OUTPUT_FEATURES)
print(f"Saved model -> {OUTPUT_MODEL}")
print(f"Saved feature list -> {OUTPUT_FEATURES}")
