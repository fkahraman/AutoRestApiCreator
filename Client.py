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

    builder = ConcreteBuilder(Method='post', Endpoint='upload',  Keys=['mail', 'apikey'])
    builder2 = ConcreteBuilder(Method='get', Endpoint='image', ExLibs=['base64', 'json'], Keys=['mail', 'apikey'])
    builder3 = ConcreteBuilder(Method='post', Endpoint='record', Keys=['mail', 'apikey', 'loc'])

    director.builder = builder
    director.build_RestFul()

    director.builder = builder2
    director.build_RestFul()

    director.builder = builder3
    director.build_RestFul()

    builder.product.list_parts()
    builder2.product.list_parts()
    builder3.product.list_parts()

    builder.product.createPy(fileName="APIs/deneme")
    builder2.product.createPy(fileName="APIs/deneme")
    builder3.product.createPy(fileName="APIs/deneme")





