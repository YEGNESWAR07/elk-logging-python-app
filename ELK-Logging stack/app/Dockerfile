FROM python:3.9.18-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY logger.py .

CMD ["python", "logger.py"]
CMD ["python", "logger.py"]

