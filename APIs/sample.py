import flask
from flask import Flask, request, jsonify, send_file
import json
import base64

app = Flask(__name__)



@app.route('/upload', methods=['POST', 'PUT'])
def getUpload():
	if flask.request.method == 'POST':
		apikey = request.values.get(key='apikey')
		mail = request.values.get(key='mail')
		
	if flask.request.method == 'PUT':
		apikey = request.values.get(key='apikey')
		updateItem = request.values.get(key='updateItem')
		
	
@app.route('/image', methods=['GET'])
def getImage():
	if flask.request.method == 'GET':
		imageID = request.args.get(key='imageID')
		
	
@app.route('/info', methods=['POST', 'GET'])
def getInfo():
	if flask.request.method == 'POST':
		userId = request.values.get(key='userId')
		token = request.values.get(key='token')
		
	if flask.request.method == 'GET':
		userId = request.args.get(key='userId')
		
	


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=9876, debug=False, threaded=True)