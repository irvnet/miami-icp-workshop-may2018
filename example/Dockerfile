# build: docker build -t irvingr/flask-sample:latest .
# run:   docker run -d -p 18080:18080 irvingr/flask-sample:latest

FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential curl

RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
EXPOSE 18080 
CMD ["app.py"]

