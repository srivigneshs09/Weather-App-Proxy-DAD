FROM python:3.9

WORKDIR /app
COPY app.py /app/
COPY templates /app/templates

RUN pip install flask requests

EXPOSE 5002
CMD ["python", "app.py"]
