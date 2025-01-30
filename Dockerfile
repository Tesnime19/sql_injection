FROM python:3.12-slim

# Install dependencies
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

# Expose port and run app
EXPOSE 8080
CMD ["python", "app/routes.py"]
