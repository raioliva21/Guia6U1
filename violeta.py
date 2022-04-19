#!/usr/bin/env python3
from plant import Plant

class Violeta(Plant):
    def __init__(self):
        super().__init__()
        # atributo publico
        self.letra = "V"