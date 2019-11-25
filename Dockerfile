FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && \
  apt-get install -y supervisor nginx git postgresql-client

# Setup the working directory
RUN mkdir /app && mkdir /home/app
WORKDIR /app
ENV HOME /home/app

# Copy application code
COPY . /app
