

  <!-- 🔝 Dashboard Image -->
  <div class="image-box">
    <img src="final_output_page.png" alt="AI Temperature Forecasting Dashboard">
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
