from flask import Flask, request
import logging
import os

app = Flask(__name__)

# Ensure logs directory exists
LOG_DIR = "/logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "requests.log")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route("/log", methods=["POST"])
def log_request():
    data = request.json
    location = data.get("location")
    if location:
        logging.info(f"Received request for location: {location}")
        return {"message": "Logged"}, 200
    return {"error": "Location not provided"}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
