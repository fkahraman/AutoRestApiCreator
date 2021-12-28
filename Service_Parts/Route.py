#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Route():

    def __init__(self, Endpoint=None, Method=None) -> None:
        self._endpoint = Endpoint
        self._method = Method.upper()

    def getRoute(self, ) :
        return f"@app.route('/{self._endpoint}', methods=['{self._method}'])\n"

