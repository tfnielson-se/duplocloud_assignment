# Use the official Python image from the Docker Hub
FROM python:3-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

# Install the dependencies
RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Define environment variable
ENV FLASK_APP=app.py

# Expose port 5000
EXPOSE 80

# Run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]