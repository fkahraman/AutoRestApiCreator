#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

class Main():

    def __init__(self, port) -> None:
        self._port = port

    def getMain(self):
        return f'\n\n\nif __name__ == "__main__":\n\tapp.run(host="0.0.0.0", port={self._port}, debug=False, threaded=True)'
