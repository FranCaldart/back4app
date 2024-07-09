# Base image
FROM python:3.10.8

ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /sistema

# Copy requirements file and install dependencies
COPY requirements.txt /sistema
RUN pip install -r requirements.txt

# Copy the rest of the project files
COPY . /sistema/

# Expose the server port
EXPOSE 8000

# Command to start the server
CMD ["python","manage.py","runserver","0.0.0.0:8000"]
