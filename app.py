from flask import Flask, render_template, request
import requests
from config import API_KEY

app = Flask(__name__)

# Emoji mapping based on weather condition codes
emoji_map = {
    1000: "☀️", 1003: "🌤️", 1006: "☁️", 1009: "☁️",
    1030: "🌫️", 1135: "🌫️", 1147: "🌫️",
    1063: "🌧️", 1150: "🌧️", 1153: "🌧️",
    1180: "🌧️", 1183: "🌧️", 1186: "🌧️",
    1189: "🌧️", 1192: "🌧️", 1195: "🌧️",
    1240: "🌧️", 1243: "🌧️", 1246: "🌧️",
    1066: "❄️", 1069: "❄️", 1114: "❄️", 1117: "❄️",
    1210: "❄️", 1213: "❄️", 1216: "❄️", 1219: "❄️",
    1222: "❄️", 1225: "❄️", 1255: "❄️", 1258: "❄️",
    1087: "⛈️", 1273: "⛈️", 1276: "⛈️", 1279: "⛈️", 1282: "⛈️",
    1171: "🌨️", 1201: "🌨️", 1207: "🌨️",
    1237: "🌨️", 1261: "🌨️", 1264: "🌨️",
    1198: "🧨", 1168: "🧨"
}

def fetch_weather(city):
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days=3&alerts=yes&aqi=yes"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return {"error": data["error"]["message"]}

    current = data['current']
    forecast = data['forecast']['forecastday'][0]
    location = data['location']
    condition = current['condition']
    code = condition['code']
    emoji = emoji_map.get(code, "🌈")

    is_day = current.get('is_day')
    time_status = "🌞 It's currently daytime." if is_day == 1 else "🌜 It's currently nighttime."

    rain_chance = forecast['day'].get('daily_will_it_rain', 0)
    snow_chance = forecast['day'].get('daily_will_it_snow', 0)
    rain_text = "☔ Yes" if rain_chance else "🌂 No"
    snow_text = "❄️ Yes" if snow_chance else "⛅ No"

    forecast_next = [
        f"📅 {day['date']}: {day['day']['condition']['text']} | Min: {day['day']['mintemp_c']}°C, Max: {day['day']['maxtemp_c']}°C"
        for day in data['forecast']['forecastday'][1:]
    ]

    alerts = data.get("alerts", {}).get("alert", [])
    alert_messages = []

# There are real alerts from the API
    if alerts:
        for alert in alerts:
            alert_messages.append({
                "event": alert.get("event", "Weather Alert"),
                "headline": alert.get("headline", ""),
                "desc": alert.get("desc", "")
            })
# No real alerts, add a test alert
    else:
        alert_messages.append({
            "event": "Test Alert",
            "headline": "This is a simulated alert",
            "desc": "You are seeing this because there is no real-time alert for this city."
        })


    return {
        "location": f"{location['name']}, {location['region']}, {location['country']}",
        "localtime": location['localtime'],
        "tz": location['tz_id'],
        "date": forecast['date'],
        "status": time_status,
        "emoji": emoji,
        "condition": condition['text'],
        "temp_c": current['temp_c'],
        "temp_f": current['temp_f'],
        "feels_c": current['feelslike_c'],
        "feels_f": current['feelslike_f'],
        "max_temp": forecast['day']['maxtemp_c'],
        "min_temp": forecast['day']['mintemp_c'],
        "humidity": current['humidity'],
        "wind": current['wind_kph'],
        "sunrise": forecast['astro']['sunrise'],
        "sunset": forecast['astro']['sunset'],
        "rain": rain_text,
        "snow": snow_text,
        "uv": current.get('uv', 'N/A'),
        "aqi": current.get('air_quality', {}).get('gb-defra-index', 'N/A'),
        "updated": current['last_updated'],
        "forecast_next": forecast_next,
        "alerts": alert_messages if alert_messages else None
    }

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form["city"]
        result = fetch_weather(city)
        if "error" in result:
            error = result["error"]
        else:
            weather = result
    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)










