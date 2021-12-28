# Auto RestFul Api Creator For Flask

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A program where you can create a skeleton for flask rest api by entering endpoint, method and values. In summary, after giving the parameters, the python code that will stand up with the relevant parameters will be created in the API folder.

## Usage
----
Python File: **Client.py**
**Code:**


    director = Director()

    builder = ConcreteBuilder(Method='post', Endpoint='upload',  ExLibs=['base64', 'json'], Keys=['mail', 'apikey'])
    builder2 = ConcreteBuilder(Method='get', Endpoint='image', Keys=['mail', 'apikey'])
    builder3 = ConcreteBuilder(Method='post', Endpoint='record', Keys=['mail', 'apikey', 'loc'])

    director.builder = builder
    director.build_RestFul()

    director.builder = builder2
    director.build_RestFul()

    director.builder = builder3
    director.build_RestFul()

    builder.product.list_parts()
    builder2.product.list_parts()
    builder3.product.list_parts()

    builder.product.createPy(fileName="APIs/deneme")
    builder2.product.createPy(fileName="APIs/deneme")
    builder3.product.createPy(fileName="APIs/deneme")
    
Output File: **Deneme.py**

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
	








