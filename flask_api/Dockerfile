# Use a lighter base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the application will run
EXPOSE 5000

# Specify the command to run on container start
CMD ["python", "app.py"]