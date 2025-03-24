FROM python:3.11-slim

# Working in the current directory
WORKDIR /app

# Install requirements in the image
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code
COPY . .

# Expose and run the container
EXPOSE 8000
CMD ["python", "src/manage.py", "runserver", "0.0.0.0:8000"]
