FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . /code/