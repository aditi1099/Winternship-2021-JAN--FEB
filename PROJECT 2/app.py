from flask import Flask 

app = Flask(__name__)

@app.route("/")
def dummy_api():
	return "Welcome to Widya Internship Project 2 Web Development!"

@app.route("/Hi/<username>")
def greet(username):
	return f"Hey You Beautiful, {username}!"

@app.route("/Hi")
def who():
	return "Well done you succesfully completed task 2 "

