
FROM python:3.9-slim
COPY ./backend /app/backend


# Install dependencies
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Node.js for frontend
RUN apt-get update && apt-get install -y nodejs npm

# Copy frontend files into the container
COPY ./frontend /app/frontend

# Install Node dependencies for frontend
WORKDIR /app/frontend
RUN npm install

# Copy application files
COPY . .

# Expose port and run the app
EXPOSE 8000
CMD ["uvicorn", "backend_fatigue_api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
CMD ["uvicorn", "backend.backend_fatigue_api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
