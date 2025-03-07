# Use the official Python image as a base
FROM python:3.11.8

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements first (to leverage Docker cache)
COPY requirements.txt /app/

# Install dependencies (optimized with --no-cache-dir)
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Start the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "school.wsgi:application"]
