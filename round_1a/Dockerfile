# Use a lightweight base image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy your app code into the container
COPY ./app /app

# Install required Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Set default command to run your main script
CMD ["python", "main.py"]
