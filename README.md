<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🌡️ AI Temperature Forecasting & Safety Alert System</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <style>
    body {
      margin: 0;
      font-family: "Segoe UI", Arial, sans-serif;
      background: linear-gradient(135deg, #2b1055, #4b1d6b, #1a0933);
      color: #f5f5f5;
      line-height: 1.7;
    }

    .container {
      max-width: 1100px;
      margin: auto;
      padding: 30px;
    }

    h1, h2, h3 {
      color: #ffd86b;
    }

    h1 {
      text-align: center;
      margin-top: 20px;
    }

    hr {
      border: none;
      height: 1px;
      background: rgba(255,255,255,0.15);
      margin: 40px 0;
    }

    ul, ol {
      margin-left: 20px;
    }

    li {
      margin-bottom: 8px;
    }

    code {
      background: rgba(255,255,255,0.1);
      padding: 4px 8px;
      border-radius: 6px;
      color: #00ffd5;
    }

    pre {
      background: rgba(0,0,0,0.4);
      padding: 15px;
      border-radius: 12px;
      overflow-x: auto;
    }

    /* 🔝 Top Image Section */
    .image-box {
      text-align: center;
      margin-bottom: 40px;
    }

    .image-box img {
      width: 100%;
      max-width: 1000px;
      border-radius: 18px;
      box-shadow: 0 15px 40px rgba(0,0,0,0.5);
    }

    .tag {
      display: inline-block;
      background: #00c6ff;
      color: #000;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 14px;
      margin: 6px 6px 6px 0;
      font-weight: 600;
    }

    .footer {
      text-align: center;
      margin-top: 50px;
      font-size: 14px;
      opacity: 0.9;
    }
  </style>
</head>

<body>

<div class="container">

  <!-- 🔝 Dashboard Image -->
  <div class="image-box">
    <img src="images/dashboard.png" alt="AI Temperature Forecasting Dashboard">
  </div>

  <h1>🌡️ AI Temperature Forecasting & Safety Alert System</h1>

  <p>
    An <b>AI-powered temperature forecasting system</b> built using
    <b>Python, Machine Learning, and Flask</b>.  
    The system predicts future temperature values based on the
    <b>last 4 temperature readings (°C)</b> and provides
    <b>visual insights, safety alerts, and risk monitoring</b>
    through an interactive web dashboard 📊🚨.
  </p>

  <hr>

  <h2>🚀 Project Overview</h2>
  <p>
    This project forecasts <b>future temperature trends</b> using historical input values and classifies conditions into:
  </p>
  <ul>
    <li>✅ Normal</li>
    <li>⚠️ Risk</li>
    <li>🔥 High Risk</li>
  </ul>
  <p>
    Designed for <b>industrial safety, climate monitoring, and AI learning</b> 🏭🌍🤖.
  </p>

  <hr>

  <h2>🔑 Key Highlights</h2>
  <ul>
    <li>🌡️ Accepts 4 recent temperature readings (°C)</li>
    <li>🔮 Predicts future temperature</li>
    <li>🔁 Converts output to Celsius, Fahrenheit & Kelvin</li>
    <li>🚨 Risk alerts (True / False)</li>
    <li>📈 Trend graph & sparkline visualization</li>
    <li>🧭 Safety gauge & compass</li>
    <li>🖥️ Flask-based interactive dashboard</li>
    <li>🧠 ML-powered forecasting</li>
  </ul>

  <hr>

  <h2>🧠 How It Works</h2>
  <ol>
    <li>👤 User enters 4 temperature values (°C)</li>
    <li>⚙️ Backend processes input via ML model</li>
    <li>📊 Model predicts upcoming temperature</li>
    <li>🛡️ System converts units, checks threshold & generates alerts</li>
  </ol>

  <hr>

  <h2>📊 Safety Logic</h2>
  <ul>
    <li>⚠️ Threshold: <b>26.67°C (80°F)</b></li>
    <li>Predicted ≥ threshold → 🚨 Alert = True</li>
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

  <p>🌐 Open in browser: <code>http://127.0.0.1:5000/</code></p>

  <hr>

  <h2>🧪 Sample Input</h2>
  <pre>35, 36, 37, 38</pre>

  <h2>📤 Sample Output</h2>
  <ul>
    <li>🌡️ Predicted Temperature: <b>29.77°C</b></li>
    <li>🚨 Alert: <b>True</b></li>
    <li>🔥 Risk Level: <b>High Risk</b></li>
  </ul>

  <div class="footer">
    ⭐ Built with ❤️ using Python, Machine Learning & Flask  
    <br>Promoting AI-driven safety systems 🌍🤖
  </div>

</div>

</body>
</html>
