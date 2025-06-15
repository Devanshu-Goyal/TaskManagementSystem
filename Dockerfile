FROM python:3.11-slim

WORKDIR /app

# Install deps first to leverage cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Now add rest of files
COPY . .

ENV FLASK_ENV=production

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "run:app"]
