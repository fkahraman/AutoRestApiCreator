#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Libraries():

    def __init__(self, libs=None) -> None:
        self._parts = ["import flask","from flask import Flask, request, jsonify, send_file"]
        self._libs = libs

        self.add()
        self.convertLibs()

    def add(self) -> None:
        for lib in self._libs:
            self._parts.append(f"import {lib}")

    def convertLibs(self):
        self.code = ""
        for line in self._parts:
            self.code += line
            self.code += '\n'
        self.code += '\napp = Flask(__name__)\n\n\n'

    def getLibs(self):
        return self.code
