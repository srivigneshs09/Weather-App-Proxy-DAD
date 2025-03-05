FROM python:3.9

WORKDIR /app
COPY weather_service.py /app/

RUN pip install flask requests

EXPOSE 5001
CMD ["python", "weather_service.py"]
