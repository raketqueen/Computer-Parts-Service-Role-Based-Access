FROM python:3.12-slim

WORKDIR /app
COPY . /app

# Install Flask and MySQL connector
RUN pip install flask mysql-connector-python

EXPOSE 5000
CMD ["python3", "app.py"]
