FROM python:3.8-alpine

LABEL maintainer="DiptiBagal"

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "./Project_Demo.py" ]
