from flask import Flask
import webbrowser, logging


app = Flask(__name__)
logging.basicConfig(level=logging.WARNING)

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
	app.run()