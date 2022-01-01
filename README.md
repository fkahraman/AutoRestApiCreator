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
Output File: **APIs/sample.py**

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
	
----

        Author : Fatih Kahraman
        Main   : fatih.khrmn@hotmail.com
