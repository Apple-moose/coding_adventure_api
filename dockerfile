# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app

# Expose the port (optional, as it's already done in the base image)
EXPOSE 80

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Command to run the app
CMD ["uvicorn", "your_module:app", "--host", "0.0.0.0", "--port", "80"]