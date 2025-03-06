FROM python:3.9

WORKDIR /app

# Copy the sidecar service code
COPY . .

# Install dependencies
RUN pip install flask requests

# Ensure logs directory exists
RUN mkdir -p /logs

# Set the log file permissions
RUN touch /logs/requests.log && chmod 666 /logs/requests.log

# Start the Sidecar service
CMD ["python", "sidecar.py"]
