FROM python:latest

RUN apt-get update && \
    apt-get install -y stress-ng && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY main.py .

RUN pip install -r requirements.txt
CMD ["python", "main.py"]
