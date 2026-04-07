from flask import Flask, request, jsonify, send_from_directory, redirect
from flask_cors import CORS
import joblib, os, traceback, numpy as np, pandas as pd

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Model loading
MODEL_FILE = "xgb_model_combined.joblib"
FEATURE_FILE = "feature_info_combined.joblib"

model = None
FEATURES = None

if os.path.exists(MODEL_FILE) and os.path.exists(FEATURE_FILE):
    try:
        model = joblib.load(MODEL_FILE)
        FEATURES = joblib.load(FEATURE_FILE)
        print("[INFO] Model and features loaded")
    except Exception as e:
        print("[ERROR] Loading model failed:", e)
        traceback.print_exc()
else:
    print("[WARN] Model files not found.")

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    response.headers['Access-Control-Allow-Origin'] = origin if origin else '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route("/predict", methods=["POST", "OPTIONS"])
def predict():
    if request.method == "OPTIONS":
        return jsonify({}), 200

    if model is None:
        return jsonify({"error": "Model not loaded"}), 500

    try:
        data = request.get_json(force=True)
        timestamps = data.get("timestamps")
        temps = data.get("temps")

        series = list(map(float, temps))
        last_ts = pd.to_datetime(timestamps[-1])

        feat = {}
        feat["hour"] = last_ts.hour
        feat["day"] = last_ts.day
        feat["weekday"] = last_ts.weekday()

        for f in FEATURES:
            if f.startswith("lag_"):
                n = int(f.split("_")[1])
                feat[f] = series[-n] if len(series) >= n else series[0]

            elif f.startswith("roll_mean_"):
                k = int(f.split("_")[-1])
                vals = series[-k:] if len(series) >= k else series
                feat[f] = float(np.mean(vals))

            elif f.startswith("roll_std_"):
                k = int(f.split("_")[-1])
                vals = series[-k:] if len(series) >= k else series
                feat[f] = float(np.std(vals))

        X = np.array([feat.get(feat_name, 0.0) for feat_name in FEATURES]).reshape(1, -1)

        pred_c = float(model.predict(X)[0])
        pred_f = pred_c * 9.0/5.0 + 32.0
        alert_f80 = pred_f >= 80.0

        return jsonify({
            "predicted_temperature_c": pred_c,
            "predicted_temperature_f": pred_f,
            "alert_f80": alert_f80
        })

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": "server error", "detail": str(e)}), 500

@app.route('/')
def root():
    return redirect('/demo.html')

@app.route('/demo.html')
def serve_demo():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(base_dir, 'demo.html')

# ✅ IMPORTANT CHANGE HERE
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))  # ✅ FIXED FOR DEPLOYMENT
    )
