FROM python:3.6.5-alpine3.7

MAINTAINER "kaajavi"
LABEL project="docker-django"
LABEL version = "1.0.0"
LABEL author_email="javierguignard@gmail.com"

COPY . /app

WORKDIR /app

RUN python3.6 -m pip install --no-cache-dir -r requirements.txt

RUN python3.6 manage.py makemigrations ; exit 0
RUN python3.6 manage.py migrate ; exit 0


EXPOSE 80

ENTRYPOINT [ "python3.6" ]

CMD [ "manage.py", "runserver", "0.0.0.0:80"]