FROM node:18-alpine

ADD . /app

WORKDIR /app

RUN npm install

EXPOSE 8000

ENTRYPOINT [ "npm" ]

CMD [ "start" ]