FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN set -ex \
    && pip install --upgrade pip \
    && pip install -r /app/requirements.txt

# Copy project
COPY . /code/