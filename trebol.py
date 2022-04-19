#!/usr/bin/env python3
from plant import Plant

class Trebol(Plant):
    def __init__(self):
        super().__init__()
        # atributo publico
        self.letra = "T"