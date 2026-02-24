FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask runs on 5000 inside container
EXPOSE 5000

# Use python directly (simple for beginners)
CMD ["python", "app.py"]