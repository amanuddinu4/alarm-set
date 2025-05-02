# Use a Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY alarm.py .

# Add the audio file to the container
COPY audio.mp3 .

# Install required Python packages
RUN pip install pygame

# Expose a default port (optional, for flexibility in container networking)
EXPOSE 8080

# Command to run the Python alarm app
CMD ["python", "alarm.py"]
