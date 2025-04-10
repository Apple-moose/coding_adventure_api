# Use official Python image as a base
FROM python:3.9-slim

# Set working directory in the container
WORKDIR /app

# Copy your FastAPI application into the container
COPY . /app

# Install dependencies (make sure you have a requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
EXPOSE 7500

# Command to run the app using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7500", "--reload"]
