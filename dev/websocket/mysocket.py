from flask import Flask, render_template, request, redirect
import os 

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
	return render_template('mainpage.html')

@app.route('/name', methods=['POST'])
def myname():
	username = request.form['name']
	return username.upper()

@app.route('/address', methods=['POST'])
def address():
	address = request.form['address']

@app.route('/find_person', methods=['GET'])
def find_person():
	username = request.args.get('name')
	# find 
	return username

if __name__ == '__main__':
	app.run()