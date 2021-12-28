#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from abc import ABC, abstractmethod
from Creator import Creator

from Service_Parts.Function import Function
from Service_Parts.Libraries import Libraries
from Service_Parts.Route import Route

class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_libraries(self) -> None:
        pass

    @abstractmethod
    def produce_part_route(self) -> None:
        pass

    @abstractmethod
    def produce_part_function(self) -> None:
        pass

class ConcreteBuilder(Builder):

    def __init__(self, Endpoint=None, Method=None, ExLibs=None, Keys=None) -> None:
        self._endpoint = Endpoint
        self._method = Method
        self._keys = Keys
        self._exLibs = ExLibs
        self.reset()

    def reset(self) -> None:
        self._product = Creator()


    @property
    def product(self) -> Creator:
        product = self._product
        #self.reset()
        return product

    def produce_part_libraries(self) -> None:
        library = Libraries(self._exLibs)
        self.libCode = library.getLibs()
        self.product.add(self.libCode)

    def produce_part_route(self) -> None:
        route = Route(Endpoint=self._endpoint, Method=self._method)
        self.routeCode = route.getRoute()
        self.product.add(self.routeCode)

    def produce_part_function(self) -> None:
        func = Function(Endpoint=self._endpoint, Method=self._method, Keys=self._keys)
        self.funcCode = func.getFunction()
        self.product.add(self.funcCode)