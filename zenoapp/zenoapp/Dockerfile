FROM python:3.7.0

# set work directory
WORKDIR /usr/src/zenoapp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/zenoapp/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/zenoapp/
