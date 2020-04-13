# pull official base image
FROM python:3.8.2

# set work directory
WORKDIR /usr/src/books_crud

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /usr/src/books_crud/requirements.txt

# install dependencies
RUN set -eux \
    && pip install -r /usr/src/books_crud/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . /usr/src/books_crud
