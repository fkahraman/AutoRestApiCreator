#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Function():

    def __init__(self, Endpoint=None, Method=None, Keys=None) -> None:
        self._endpoint = Endpoint
        self._method = Method.upper()
        self._keys = Keys
        self._readKeys = []

        self.prepareFuncName()
        self.prepareKeys()

    def prepareFuncName(self):
        self.funcName = f"def get{self._endpoint.capitalize()}():"

    def prepareKeys(self):

        if self._method == 'POST':
            for key in self._keys:
                self._readKeys.append(f"{key} = request.values.get(key='{key}')")

        elif self._method == 'GET':
            for key in self._keys:
                self._readKeys.append(f"{key} = request.args.get(key='{key}')")

        else:
            pass

    def convertString(self):
        text = ""
        for line in self._readKeys:
            text += line
            text += '\n\t\t'
        return text

    def getFunction(self):
        head = f"{self.funcName}"
        permission = f"\n\tif flask.request.method == '{self._method}':"
        keys = f"\n\t\t{self.convertString()}\n\n\n\telse:\n\t\t"
        end = "return jsonify({'Message': 'Wrong Key!'})\n\n\n"

        return head+permission+keys+end


