import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

WEATHER_SERVICE_URL = "http://weather_service:5001/weather"

@app.route('/weather', methods=['GET'])
def proxy_weather():
    location = request.args.get("location", "New York")
    response = requests.get(WEATHER_SERVICE_URL, params={"location": location})

    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
