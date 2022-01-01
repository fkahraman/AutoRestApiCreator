#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from typing import Any

class Creator():

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"{''.join(self.parts)}", end="")

    def createPy(self, fileName = None):
        f = open(f'APIs/{fileName}.py', 'a+')
        for part in self.parts:
            f.write(part)
        f.close()