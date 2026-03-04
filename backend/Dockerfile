FROM python:3.10.20-alpine

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]