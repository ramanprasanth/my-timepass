FROM ubuntu:latest
RUN apt-get update && apt-get install -y python3.6 && apt-get install -y python-pip
RUN pip install flask
EXPOSE 8000
COPY main.py  .
CMD ["python","main.py"]