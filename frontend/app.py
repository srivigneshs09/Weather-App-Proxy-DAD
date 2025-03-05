import requests
from flask import Flask, render_template, request

app = Flask(__name__)

PROXY_URL = "http://ambassador_proxy:5000/weather"

@app.route("/", methods=["GET", "POST"])
def home():
    weather_data = None
    if request.method == "POST":
        location = request.form.get("location")
        response = requests.get(PROXY_URL, params={"location": location})
        weather_data = response.json()
    return render_template("index.html", weather=weather_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002)
