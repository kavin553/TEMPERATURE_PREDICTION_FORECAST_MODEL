🌡️ AI Temperature Forecasting & Safety Alert System
An AI-powered temperature forecasting system built using Python, Machine Learning, and Flask. The system predicts future temperature values based on the last 4 temperature readings (°C) and provides visual insights, safety alerts, and risk monitoring through an interactive web dashboard 📊🚨.

🚀 Project Overview
This project forecasts future temperature trends using historical input values and classifies the situation into:

✅ Normal
⚠️ Risk
🔥 High Risk
Designed for industrial safety, climate monitoring, and AI learning purposes 🏭🌍🤖.

🔑 Key Highlights
🌡️ Accepts 4 recent temperature readings (°C)
🔮 Predicts future temperature
🔁 Converts output to Celsius, Fahrenheit, and Kelvin
🚨 Displays risk alerts (True / False)
📈 Visualizes trend graphs & sparkline
🧭 Provides safety gauge & compass
🖥️ Flask-based interactive dashboard
🧠 Machine Learning powered prediction
🧠 How It Works
👤 User inputs 4 temperature values (°C)
⚙️ Backend processes data using ML model
📊 Model predicts the next temperature
🛡️ System converts units, checks threshold, generates alerts, and classifies risk
🖥️ Web Interface Features
🔹 Input Section
Enter 4 temperature readings (°C) separated by commas

🔹 Prediction Output
🌡️ Celsius (°C)
🔥 Fahrenheit (°F)
❄️ Kelvin (K)
🔹 Safety Monitoring
🚨 Alert Status: True / False
📌 Risk Level: Normal / Risk / High Risk
🔹 Visualization
📉 Line chart (historical + predicted)
📈 Sparkline trend
🌡️ Temperature gauge
🧭 Safety compass
📊 Safety Logic
⚠️ Threshold: 26.67°C (80°F)
If predicted ≥ threshold → 🚨 Alert = True
Else → ✅ Safe condition
🛠️ Technologies Used
Flask
Flask-CORS
Joblib
NumPy
Pandas
Scikit-learn
XGBoost
Matplotlib
Seaborn
Pytest
⚙️ Installation & Setup
git clone https://github.com/your-username/temperature-forecasting-ai.git
cd temperature-forecasting-ai
pip install -r requirements.txt
python app.py
🌐 Open browser: http://127.0.0.1:5000/

🧪 Sample Input
35, 36, 37, 38
📤 Sample Output
🌡️ Predicted Temperature: 29.77°C
🚨 Alert: True
🔥 Risk Level: High Risk
📌 Future Enhancements
🌐 Live weather API integration
📅 Multi-day forecasting
☁️ Cloud deployment (AWS / Render)
📱 Mobile-friendly UI
📡 Real-time sensor data
⭐ Built with ❤️ using Python, Machine Learning & Flask
Promoting AI-driven safety systems 🌍🤖
