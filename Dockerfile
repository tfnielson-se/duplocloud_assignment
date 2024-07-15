FROM --platform=linux/amd64 python:3-slim-buster AS build

WORKDIR /app

COPY requirements.txt /app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["python3", "app.py"]