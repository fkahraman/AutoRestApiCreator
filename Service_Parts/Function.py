#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Function():

    def __init__(self, config) -> None:
        self._config = config
        self.parseConfig()

        self._readKeys = {}

        self.prepareFuncName()
        self.prepareKeys()

    def parseConfig(self):
        self._endpoint = self._config["Endpoint"]
        self._methods = self._config["Methods"]

    def getCode(self, schema):
        text = "\n\t"
        for head in schema.keys():
            text += head
            text += '\n\t\t'
            for item in schema[head]:
                text += item
                text += '\n\t\t'
            text += '\n\t'
        return text

    def methodFilter(self, variable):
        allow = ['POST', 'GET', 'PUT', 'DELETE']
        if (variable.upper() in allow):
            return True
        else:
            return False

    def prepareFuncName(self):
        self.funcName = f"def get{self._endpoint.capitalize()}():"

    def prepareKeys(self):
        cache = []
        for method in self._methods.keys():
            if filter(self.methodFilter, method.upper()):
                if method.upper() == 'POST':
                    for key in self._methods[method.upper()].keys():
                        cache.append(f"{key} = request.values.get(key='{key}')")
                    self._readKeys["if flask.request.method == 'POST':"] = cache
                    cache = []

                if method.upper() == 'GET':
                    for key in self._methods[method.upper()].keys():
                        cache.append(f"{key} = request.args.get(key='{key}')")
                    self._readKeys["if flask.request.method == 'GET':"] = cache
                    cache = []

                if method.upper() == 'PUT':
                    for key in self._methods[method.upper()].keys():
                        cache.append(f"{key} = request.values.get(key='{key}')")
                    self._readKeys["if flask.request.method == 'PUT':"] = cache
                    cache = []

                if method.upper() == 'DELETE':
                    for key in self._methods[method.upper()].keys():
                        cache.append(f"{key} = request.values.get(key='{key}')")
                    self._readKeys["if flask.request.method == 'DELETE':"] = cache
                    cache = []
        else:
            pass

    def getFunction(self):
        head = f"{self.funcName}"
        body = self.getCode(self._readKeys)
        return head+body
