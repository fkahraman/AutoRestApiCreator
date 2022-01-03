# Auto RestFul Api Creator For Flask

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

A program where you can create a skeleton for flask rest api by entering endpoint, method and values. In summary, after giving the parameters, the python code that will stand up with the relevant parameters will be created in the API folder.

## Usage
----
Sample Config File: **Config/config.json**

```
{
  "Services": {
    "Rest1": {
      "Endpoint": "upload",
      "Methods": {
        "POST": {
          "apikey": "Kirel",
          "mail": "kirel@kirel.com"
        },
        "PUT": {
          "apikey": "Kirel",
          "updateItem": "KirelItem"
        }
      }
    },
    "Rest2": {
      "Endpoint": "image",
      "Methods": {
        "GET": {
          "imageID": "64"
        }
      }
    },
    "Rest3": {
      "Endpoint": "info",
      "Methods": {
        "POST": {
          "userId": "25",
          "token": "88STT893ASDD0"
        },
        "GET": {
          "userId": 25
        }
      }
    }
  },
  "ExtraLibs": [
    "json",
    "base64"
  ],
  "Port": "9876"
}
```

Run File: **Client.py**
----
Output File: **APIs/sample.py**

```

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
		
```

        Author : Fatih Kahraman
        Main   : fatih.khrmn@hotmail.com
