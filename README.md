# 🌤️ Weather App Proxy (Ambassador Pattern)

This is a **Dockerized Weather App** that uses the **Ambassador Pattern** to fetch real-time weather data from [WeatherAPI.com](https://www.weatherapi.com/). It consists of a **Flask-based frontend**, an **Ambassador Proxy**, and a **Weather Service**.

---

## 🚀 Features

- ✅ Fetches real-time weather data based on user input  
- ✅ Uses **Ambassador Pattern** to forward API requests  
- ✅ Built with **Flask** and **Dockerized** using **Docker Compose**  
- ✅ Simple and clean UI  

---

## 📂 Project Structure

Weather-App-Proxy/
│── weather_service/
│   ├── weather_service.py    # Fetches weather data
│   ├── Dockerfile
│── ambassador_proxy/
│   ├── ambassador_proxy.py   # Forwards requests to weather service
│   ├── Dockerfile
│── frontend/
│   ├── app.py                # Flask frontend
│   ├── templates/
│   │   ├── index.html        # UI page
│   ├── Dockerfile
│── docker-compose.yml
│── README.md

---

### 1️. Clone the Repository
git clone https://github.com/your-username/weather-app-proxy.git
cd weather-app-proxy

## 🛠️ How to Run

1. Add Your WeatherAPI Key
Open weather_service/weather_service.py and replace "your_weatherapi_key" with your actual API key from WeatherAPI.com.

2. Run the Application
docker-compose up --build

4️⃣ Open in Browser
Frontend UI: http://localhost:5002
Ambassador Proxy: http://localhost:5000/weather?location=Madurai
Weather Service: http://localhost:5001/weather?location=Madurai
