#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from Director import Director
from Builder import ConcreteBuilder

if __name__ == "__main__":

    director = Director()

    builder = ConcreteBuilder()

    director.builder = builder
    director.build_RestFul()

    builder.product.list_parts()

    builder.product.createPy(fileName="sample")
