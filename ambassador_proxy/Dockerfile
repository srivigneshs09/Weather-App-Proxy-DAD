FROM python:3.9

WORKDIR /app
COPY ambassador_proxy.py /app/

RUN pip install flask requests

EXPOSE 5000
CMD ["python", "ambassador_proxy.py"]
