from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

WEATHER_SERVICE_URL = "http://weather_service:5001/weather"
SIDECAR_URL = "http://sidecar:5003/log"

@app.route("/weather")
def get_weather():
    location = request.args.get("location")
    
    # Log request via Sidecar
    requests.post(SIDECAR_URL, json={"location": location})

    # Forward request to Weather Service
    response = requests.get(f"{WEATHER_SERVICE_URL}?location={location}")
    return response.json()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
