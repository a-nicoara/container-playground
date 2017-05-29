FROM python:3.6.1-alpine

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY customer.py /usr/src/app

VOLUME ./customer:/usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./customer.py" ]
