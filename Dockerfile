FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3.6 && apt-get install -y python3-pip
RUN pip3 install flask
EXPOSE 5000
COPY main.py  .
CMD ["python","main.py"]