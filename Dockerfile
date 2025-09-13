FROM python:3.11-slim

# Install netcat for database connection checking
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Make entrypoint script executable
RUN chmod +x entrypoint.sh

EXPOSE 8000

CMD ["bash", "./entrypoint.sh"]