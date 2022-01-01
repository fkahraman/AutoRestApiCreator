#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Route():

    def __init__(self, config) -> None:
        self._config = config
        self.parseConfig()
        self._method = filter(self.methodFilter, self._method)
        self._methodBlock = []
        self.setMethodBlock()

    def parseConfig(self):
        self._method = []
        self._endpoint = self._config["Endpoint"]
        for methods in self._config["Methods"].keys():
            self._method.append(methods.upper())

    def methodFilter(self, variable):
        allow = ['POST', 'GET', 'PUT', 'DELETE']
        if (variable.upper() in allow):
            return True
        else:
            return False

    def setMethodBlock(self):
        for kind in self._method:
            self._methodBlock.append(kind.upper())

    def getRoute(self, ) :
        return f"\n@app.route('/{self._endpoint}', methods={self._methodBlock})\n"
