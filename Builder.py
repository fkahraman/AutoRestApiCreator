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
from Service_Parts.Main import Main

import json

class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_libraries(self, libs) -> None:
        pass

    @abstractmethod
    def produce_part_route(self, config) -> None:
        pass

    @abstractmethod
    def produce_part_function(self, config) -> None:
        pass

    @abstractmethod
    def produce_part_main(self, port) -> None:
        pass

class ConcreteBuilder(Builder):

    #   Daha sonrasında config dosyası API ile kullanılabilsin diye config parametresinin
    #   None olup olmamasına göre işlem yapılacak.
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Creator()

    @property
    def product(self) -> Creator:
        product = self._product
        #self.reset()
        return product

    def produce_part_libraries(self, libs) -> None:
        library = Libraries(libs)
        self.libCode = library.getLibs()
        self.product.add(self.libCode)

    def produce_part_route(self, config) -> None:
        route = Route(config)
        self.routeCode = route.getRoute()
        self.product.add(self.routeCode)

    def produce_part_function(self, config) -> None:
        func = Function(config)
        self.funcCode = func.getFunction()
        self.product.add(self.funcCode)

    def produce_part_main(self, port) -> None:
        main = Main(port)
        self.mainCode = main.getMain()
        self.product.add(self.mainCode)


