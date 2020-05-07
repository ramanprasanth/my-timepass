from flask import Flask
import webbrowser, logging
import os, datetime

app = Flask(__name__)
current_directory = os.getcwd()
if not os.path.isdir(current_directory+"/logs"):
	os.mkdir(current_directory+"/logs")
current_time = datetime.datetime.strftime(datetime.datetime.now(), "%d%m%Y%H%M%S")
create_logfile = current_directory+"/logs/logs_"+current_time+".txt"
logging.basicConfig(filename=create_logfile, level=20)

@app.route('/', methods=["GET"])
def home():
	logging.info("coming to home route")
	return "<a href='/next'>Go to Next</a> </br> Hello.. Welcome to my world !!"

@app.route('/next', methods=["GET"])
def next():
	logging.info("coming to next route")
	return "<a href='/'>Go back</a> </br> Hello.. Welcome to next page of my world !!"


if __name__ == "__main__":
	webbrowser.open_new("http://127.0.0.1:5000/")
	app.run(host="0.0.0.0", port="5000")