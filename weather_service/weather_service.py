from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "4fa7cd43aab047bea01194738250503"
API_URL = "http://api.weatherapi.com/v1/current.json"

@app.route("/weather")
def get_weather():
    location = request.args.get("location")
    response = requests.get(f"{API_URL}?key={API_KEY}&q={location}")
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "location": data["location"]["name"],
            "temperature": data["current"]["temp_c"],
            "condition": data["current"]["condition"]["text"],
            "humidity": data["current"]["humidity"],
            "wind_speed": data["current"]["wind_kph"]
        }
        return jsonify(weather_info)
    else:
        return jsonify({"error": "Unable to fetch weather data"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
