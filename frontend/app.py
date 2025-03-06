from flask import Flask, render_template, request
import requests

app = Flask(__name__)

AMBASSADOR_URL = "http://ambassador:5000/weather"

@app.route("/", methods=["GET", "POST"])
def index():
    weather = None
    if request.method == "POST":
        location = request.form["location"]
        response = requests.get(f"{AMBASSADOR_URL}?location={location}")
        weather = response.json()
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
