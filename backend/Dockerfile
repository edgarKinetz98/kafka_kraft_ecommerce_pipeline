FROM --platform=linux/arm64 python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY consumer.py .

CMD ["python", "app.py"]