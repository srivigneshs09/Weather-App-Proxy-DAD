FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install flask requests
CMD ["python", "ambassador_proxy.py"]
