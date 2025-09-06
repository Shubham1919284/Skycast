# 🌦️ SkyCast – Smart Weather Assistant (Flask-Based)

> A real-time weather assistant that gives detailed forecasts, air quality insights, and region-specific alerts — with a polished Flask UI and voice input.

SkyCast is built using **Python + Flask** and allows users to check weather conditions for any city around the world.  
It combines real-time weather data with a clean UI, emoji-enhanced display, and browser-based voice input for a modern, user-friendly experience.

---

## 🖼️ Screenshots

| UI Home | Forecast View | Voice Input | Weather Alerts |
|--------|----------------|----------------|-------------|
| ![UI](./Screenshot%202025-07-07%20124638.png) | ![Forecast](./Screenshot%202025-07-07%20124702.png) | ![Alert](./Screenshot%202025-07-07%20124834.png) | ![Voice](./Screenshot%202025-07-07%20124851.png) |

---

## 🌟 Features

- 🔍 **3-Day Forecast** (temperature, humidity, wind, UV index)
- 🌡️ **Feels Like Temperature** in °C and °F
- 🌫️ **Air Quality Index (AQI)** classification (DEFRA-based)
- ⚠️ **Live Weather Alerts** (storm, flood, snow, etc.)
- 🎤 **Voice-enabled Search** using browser speech recognition
- 🖼️ **Emoji-based UI** with sunrise/sunset times
- 🧭 Shows **timezone**, **last updated**, and **location data**

---

## 🧠 What This Project Demonstrates

- API integration using `requests`  
- Flask web app development with HTML + CSS  
- Voice input using JavaScript’s `webkitSpeechRecognition`  
- Structuring real-time data in a user-friendly layout  
- Smart use of visuals (icons, colors, layout) to improve UX

---

## 🛠️ Tech Stack

| Layer       | Technology Used               |
|-------------|-------------------------------|
| Backend     | Python, Flask                 |
| Frontend    | HTML, CSS (inline & custom)  |
| API         | [WeatherAPI](https://www.weatherapi.com) |
| Voice Input | JavaScript (Web Speech API)   |

---

## 📂 Project Structure

skycast/
│
├── app.py # Flask backend logic
├── templates/
│ └── index.html # UI template
├── config.py # WeatherAPI key (user-created)
├── requirements.txt # All dependencies
├── static/ # (Optional) additional assets
└── README.md


## ⚙️ How to Run the Project

> Follow these steps to run the Flask-based SkyCast app locally:

1. **Clone the repository**
   ```bash
git clone https://github.com/your-username/skycast.git
cd skycast

2.  Install dependencies
    ```bash
pip install -r requirements.txt

3. Replace API_KEY
API_KEY = "your_actual_weatherapi_key"

4. Run The File
python app.py

Open http://127.0.0.1:5000 in your browser.

-----

💬 Example City Searches
1. Delhi

2. New York

3. Tokyo

4. Southen Hamburg (has alerts during storm/flood conditions)

----

🙌 Credits
Weather data provided by WeatherAPI.com

Voice recognition via browser-native Web Speech API (Chrome preferred)

----

📄 License
This project is licensed under the MIT License.
Feel free to explore, enhance, or build upon SkyCast for your own weather-based applications.

----

👋 Author
Made with ❤️ by [Your Name]
For questions, feedback, or collaborations, feel free to connect on LinkedIn.

Stay safe, stay informed — with SkyCast ⛅

---

## 👨‍💻 Author

**Shubham Kumar Jha**  
🎓 BTech CSE (Data Science), Gulzar Group of Institutes (PTU)
📧 Email: sk1919284@gmail.com
🔗 LinkedIn
💻 GitHub

