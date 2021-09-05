# pull offical image
FROM python:3.9-alpine3.14

# set enviroments varibales for python 
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


# copy the dependences
COPY ./requirements.txt /requirements.txt

# setup work directory 
# create and copy the working dirctory
RUN mkdir /app
WORKDIR /app
COPY ./app /app

# setup the Port for the Application
EXPOSE 8000

# install and upgrade the virtual python enviorment 
RUN python -m venv /py
RUN /py/bin/pip install --upgrade pip

# for postgres-db 
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-deps build-base postgresql-dev musl-dev

# install dependences
RUN /py/bin/pip install -r /requirements.txt

# delete the tmp-deps form postgtres
RUN apk del .tmp-deps

# setup the user to start the Application
RUN adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

# initial the user
USER app

