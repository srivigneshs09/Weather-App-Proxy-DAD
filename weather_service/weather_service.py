import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Replace with your actual WeatherAPI.com key
API_KEY = "4fa7cd43aab047bea01194738250503"
WEATHER_API_URL = "http://api.weatherapi.com/v1/current.json"

@app.route('/weather', methods=['GET'])
def get_weather():
    location = request.args.get("location", "Madurai")  # Default to New York if not provided

    # Fetch real-time weather data from WeatherAPI.com
    response = requests.get(WEATHER_API_URL, params={
        "key": API_KEY,
        "q": location,
        "aqi": "no"  # Disable air quality index to keep the response minimal
    })

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    data = response.json()
    weather_info = {
        "location": data["location"]["name"] + ", " + data["location"]["country"],
        "temperature": f"{data['current']['temp_c']}°C",
        "condition": data["current"]["condition"]["text"],
        "humidity": f"{data['current']['humidity']}%",
        "wind_speed": f"{data['current']['wind_kph']} kph"
    }
    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
