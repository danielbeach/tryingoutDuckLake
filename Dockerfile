FROM python:latest

RUN apt-get update && \
    apt-get install -y curl git && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Install dependencies using pip
RUN pip install --no-cache-dir duckdb pytz
