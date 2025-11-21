# Use a lightweight Python image
FROM python:3.11-slim

# Create a working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Environment variables (your real key will be passed at runtime)
ENV FLASK_ENV=production

# Command to run the app
CMD ["python", "app.py"]

