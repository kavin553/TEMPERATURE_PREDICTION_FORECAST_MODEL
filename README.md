
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌡️ AI Temperature Forecasting & Safety Alert System</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      font-family: "Segoe UI", Arial, sans-serif;
      background: linear-gradient(135deg, #2b1055, #7597de);
      color: #f5f5f5;
      line-height: 1.7;
      padding: 20px;
    }
    .container {
      max-width: 1000px;
      margin: auto;
      background: rgba(0,0,0,0.25);
      padding: 30px;
      border-radius: 15px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    h1, h2, h3 {
      color: #ffd86b;
    }
    h1 {
      text-align: center;
    }
    ul {
      margin-left: 20px;
    }
    li {
      margin-bottom: 8px;
    }
    code {
      background: rgba(255,255,255,0.1);
      padding: 4px 8px;
      border-radius: 6px;
      color: #00ffcc;
    }
    pre {
      background: rgba(0,0,0,0.4);
      padding: 15px;
      border-radius: 10px;
      overflow-x: auto;
    }
    .tag {
      display: inline-block;
      background: #00c6ff;
      color: #000;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 14px;
      margin: 5px 5px 5px 0;
    }
    .footer {
      text-align: center;
      margin-top: 40px;
      font-size: 14px;
      opacity: 0.9;
    }
  </style>
</head>
<body>

<div class="container">

<h1>🌡️ AI Temperature Forecasting & Safety Alert System</h1>

<p>
An <b>AI-powered temperature forecasting system</b> built using
<b>Python, Machine Learning, and Flask</b>.  
The system predicts future temperature values based on the <b>last 4 temperature readings (°C)</b> and provides
<b>visual insights, safety alerts, and risk monitoring</b> through an interactive web dashboard 📊🚨.
</p>

<hr>

<h2>🚀 Project Overview</h2>
<p>
This project forecasts <b>future temperature trends</b> using historical input values and classifies the situation into:
</p>
<ul>
  <li>✅ Normal</li>
  <li>⚠️ Risk</li>
  <li>🔥 High Risk</li>
</ul>
<p>
Designed for <b>industrial safety, climate monitoring, and AI learning</b> purposes 🏭🌍🤖.
</p>

<hr>

<h2>🔑 Key Highlights</h2>
<ul>
  <li>🌡️ Accepts <b>4 recent temperature readings (°C)</b></li>
  <li>🔮 Predicts future temperature</li>
  <li>🔁 Converts output to <b>Celsius, Fahrenheit, and Kelvin</b></li>
  <li>🚨 Displays risk alerts (<b>True / False</b>)</li>
  <li>📈 Visualizes trend graphs & sparkline</li>
  <li>🧭 Provides safety gauge & compass</li>
  <li>🖥️ Flask-based interactive dashboard</li>
  <li>🧠 Machine Learning powered prediction</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>
<ol>
  <li>👤 User inputs <b>4 temperature values (°C)</b></li>
  <li>⚙️ Backend processes data using ML model</li>
  <li>📊 Model predicts the next temperature</li>
  <li>🛡️ System converts units, checks threshold, generates alerts, and classifies risk</li>
</ol>

<hr>

<h2>🖥️ Web Interface Features</h2>

<h3>🔹 Input Section</h3>
<p>Enter <b>4 temperature readings (°C)</b> separated by commas</p>

<h3>🔹 Prediction Output</h3>
<ul>
  <li>🌡️ Celsius (°C)</li>
  <li>🔥 Fahrenheit (°F)</li>
  <li>❄️ Kelvin (K)</li>
</ul>

<h3>🔹 Safety Monitoring</h3>
<ul>
  <li>🚨 Alert Status: True / False</li>
  <li>📌 Risk Level: Normal / Risk / High Risk</li>
</ul>

<h3>🔹 Visualization</h3>
<ul>
  <li>📉 Line chart (historical + predicted)</li>
  <li>📈 Sparkline trend</li>
  <li>🌡️ Temperature gauge</li>
  <li>🧭 Safety compass</li>
</ul>

<hr>

<h2>📊 Safety Logic</h2>
<ul>
  <li>⚠️ Threshold: <b>26.67°C (80°F)</b></li>
  <li>If predicted ≥ threshold → 🚨 Alert = True</li>
  <li>Else → ✅ Safe condition</li>
</ul>

<hr>

<h2>🛠️ Technologies Used</h2>

<div class="tag">Flask</div>
<div class="tag">Flask-CORS</div>
<div class="tag">Joblib</div>
<div class="tag">NumPy</div>
<div class="tag">Pandas</div>
<div class="tag">Scikit-learn</div>
<div class="tag">XGBoost</div>
<div class="tag">Matplotlib</div>
<div class="tag">Seaborn</div>
<div class="tag">Pytest</div>

<hr>

<h2>⚙️ Installation & Setup</h2>

<pre>
git clone https://github.com/your-username/temperature-forecasting-ai.git
cd temperature-forecasting-ai
pip install -r requirements.txt
python app.py
</pre>

<p>🌐 Open browser: <code>http://127.0.0.1:5000/</code></p>

<hr>

<h2>🧪 Sample Input</h2>
<pre>35, 36, 37, 38</pre>

<h2>📤 Sample Output</h2>
<ul>
  <li>🌡️ Predicted Temperature: <b>29.77°C</b></li>
  <li>🚨 Alert: <b>True</b></li>
  <li>🔥 Risk Level: <b>High Risk</b></li>
</ul>

<hr>

<h2>📌 Future Enhancements</h2>
<ul>
  <li>🌐 Live weather API integration</li>
  <li>📅 Multi-day forecasting</li>
  <li>☁️ Cloud deployment (AWS / Render)</li>
  <li>📱 Mobile-friendly UI</li>
  <li>📡 Real-time sensor data</li>
</ul>

<div class="footer">
  ⭐ Built with ❤️ using Python, Machine Learning & Flask  
  <br>Promoting AI-driven safety systems 🌍🤖
</div>

</div>
</body>
</html>

