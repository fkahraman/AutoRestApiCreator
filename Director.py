#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from Builder import Builder

class Director:

    def __init__(self) -> None:
        self._builder = None
        self.directorCommand = 1

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder


    # Sadece ilk çağrılışta ekstra kütüphaneye izin verilir.
    def build_RestFul(self) -> None:
        if self.directorCommand == 1:
            self.builder.produce_part_libraries()
            self.directorCommand -= 1
        self.builder.produce_part_route()
        self.builder.produce_part_function()

