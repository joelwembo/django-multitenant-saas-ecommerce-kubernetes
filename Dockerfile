# Use an official Python runtime as a parent image
FROM python:3.11-slim-bullseye
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set the working directory in the container
WORKDIR /app
# Copy the requirements file into the container at /app
COPY requirements.txt /app/
# COPY deployments ./app/deployments/
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
# Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -r requirements.txt
# Copy the current directory contents into the container at /app
COPY . /app/

EXPOSE 8585
