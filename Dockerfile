FROM python:3.7

ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && \
  apt-get install -y tesseract-ocr libtesseract-dev

# Setup the working directory
RUN mkdir /app && mkdir /home/app
WORKDIR /app
ENV HOME /home/app

# Install application dependencies
RUN pip install --no-cache-dir --trusted-host pypi.python.org pipenv
COPY Pipfile /app/
COPY Pipfile.lock /app/
RUN pipenv install --dev

# Copy application code
COPY . /app

# Entry
CMD pipenv run /app/demo.py
