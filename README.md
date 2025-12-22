
🌡️ AI Temperature Forecasting & Safety Alert System

An end-to-end AI-powered temperature forecasting system built using Python, Machine Learning, and Flask.
The system predicts future temperature values based on the last 4 temperature readings (°C) and provides visual insights, safety alerts, and risk monitoring through an interactive web dashboard.

🚀 Project Overview

This project forecasts future temperature trends using historical input values and classifies the situation into Normal / Risk / High Risk levels.
It is designed for industrial safety, climate monitoring, and AI learning purposes.

🔑 Key Highlights

Accepts 4 recent temperature readings (°C)

Predicts future temperature

Converts output to Celsius, Fahrenheit, and Kelvin

Displays risk alerts (True / False)

Visualizes trend graphs & sparkline

Provides safety gauge & compass

Flask-based interactive dashboard

Machine Learning powered prediction

🧠 How It Works

User inputs 4 temperature values (°C)

Backend processes data using ML model

Model predicts the next temperature

System:

Converts temperature units

Checks safety threshold

Generates alert

Classifies risk level

Dashboard visualizes:

Trend graph (past → predicted)

Sparkline

Safety gauge

Risk status

🖥️ Web Interface Features
🔹 Input Section

Enter 4 temperature readings (°C) separated by commas

🔹 Prediction Output

Predicted Temperature:

Celsius (°C)

Fahrenheit (°F)

Kelvin (K)

🔹 Safety Monitoring

Alert status: True / False

Risk Level:

✅ Normal

⚠️ Risk

🔥 High Risk

🔹 Visualization

Line chart (historical + predicted)

Sparkline trend

Temperature gauge

Safety compass

📊 Safety Logic

Threshold: 26.67°C (80°F)

If predicted temperature ≥ threshold:

🚨 Alert = True

Risk level escalates

Else:

✅ Safe condition

🛠️ Technologies Used
🔹 Backend

Flask – Web framework

Flask-CORS – Cross-origin support

Joblib – Model loading

NumPy – Numerical operations

Pandas – Data handling

🔹 Machine Learning

Scikit-learn – Model training & preprocessing

XGBoost – High-performance regression model

🔹 Visualization

Matplotlib – Graph plotting

Seaborn – Enhanced visual styling

🔹 Testing

Pytest – Unit testing

📂 Project Structure
├── app.py                # Flask application
├── model/
│   └── temperature_model.pkl
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── utils/
│   └── prediction.py
├── tests/
│   └── test_model.py
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/temperature-forecasting-ai.git
cd temperature-forecasting-ai

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run Application
python app.py

4️⃣ Open Browser
http://127.0.0.1:5000/

🧪 Sample Input
35, 36, 37, 38

📤 Sample Output

Predicted Temperature: 29.77°C

Alert: True

Risk Level: High Risk

Safety Recommendation Displayed

📈 Model Details

Algorithm: XGBoost Regressor

Input Features: Last 4 temperature readings

Output: Next predicted temperature

Optimized for:

Accuracy

Trend sensitivity

Safety detection

🔐 Use Cases

🏭 Factory temperature monitoring

🌍 Climate trend analysis

🔬 AI & ML academic projects

🧑‍💻 Portfolio & resume projects

🚨 Safety alert systems

📌 Future Enhancements

Live weather API integration

Multi-day forecasting

Cloud deployment (AWS / Render)

Mobile-friendly UI

Real-time sensor data input

User authentication

🤝 Contribution

Contributions are welcome!
Feel free to fork the repository and submit pull requests.

📜 License

This project is licensed under the MIT License.

⭐ Acknowledgements

Built with ❤️ using Python, Machine Learning, and Flask to promote AI-driven safety systems.
