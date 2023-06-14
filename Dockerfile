FROM python:3.10.6-buster

COPY requirements.txt requirements.txt
COPY bikesharing bikesharing
COPY data data

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD uvicorn taxifare.api.fast:app --host 0.0.0.0 --port $PORT
