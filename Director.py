#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
        Author : Fatih Kahraman
        Mail   : fatih.khrmn@hotmail.com
"""

from Builder import Builder
import json

class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder
        self.loadSchema()
        self.setLibConfig()
        self.setContent()
        self.setPort()

    def loadSchema(self):
        self._config = json.load(open('Config/config.json'))

    def setLibConfig(self):
        self._libConfig = self._config["ExtraLibs"]

    def setContent(self):
        self._content = self._config["Services"]

    def setPort(self):
        self._port = self._config["Port"]

    # Sadece ilk çağrılışta ekstra kütüphaneye izin verilir.
    def build_RestFul(self) -> None:
        self.builder.produce_part_libraries(self._libConfig)

        for rest in self._content.keys():
            self.builder.produce_part_route(self._content[rest])
            self.builder.produce_part_function(self._content[rest])

        self.builder.produce_part_main(self._port)
