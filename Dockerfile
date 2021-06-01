FROM ubuntu:latest

ENV PORT 80
ENV HOST 0.0.0.0

EXPOSE 80

RUN apt-get update -y && \
    apt-get install -y python3-pip
COPY ./requirements.txt /app/requirements.txt
ADD https://storage.googleapis.com/database_import_nusademy/vectorizer.pkl /app

WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]
