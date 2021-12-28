import flask
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def getUpload():
	if flask.request.method == 'POST':
		mail = request.values.get(key='mail')
		apikey = request.values.get(key='apikey')
		


	else:
		return jsonify({'Message': 'Wrong Key!'})


@app.route('/image', methods=['GET'])
def getImage():
	if flask.request.method == 'GET':
		mail = request.args.get(key='mail')
		apikey = request.args.get(key='apikey')
		


	else:
		return jsonify({'Message': 'Wrong Key!'})


@app.route('/record', methods=['POST'])
def getRecord():
	if flask.request.method == 'POST':
		mail = request.values.get(key='mail')
		apikey = request.values.get(key='apikey')
		loc = request.values.get(key='loc')
		


	else:
		return jsonify({'Message': 'Wrong Key!'})


import flask
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def getUpload():
	if flask.request.method == 'POST':
		mail = request.values.get(key='mail')
		apikey = request.values.get(key='apikey')
		


	else:
		return jsonify({'Message': 'Wrong Key!'})


@app.route('/image', methods=['GET'])
def getImage():
	if flask.request.method == 'GET':
		mail = request.args.get(key='mail')
		apikey = request.args.get(key='apikey')
		


	else:
		return jsonify({'Message': 'Wrong Key!'})


@app.route('/record', methods=['POST'])
def getRecord():
	if flask.request.method == 'POST':
		mail = request.values.get(key='mail')
		apikey = request.values.get(key='apikey')
		loc = request.values.get(key='loc')
		


	else:
		return jsonify({'Message': 'Wrong Key!'})


