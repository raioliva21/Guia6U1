#!/usr/bin/env python3
from alumno import Alumno
from plant import Plant

class Vaso():

    def __init__(self, propeetario, planta):
        self._propeetario = propeetario
        self._planta = planta
    
    @property
    def propeetario(self):
        return self._propeetario
    
    @propeetario.setter
    def propeetario(self, nombre):
        if isinstance(nombre, Alumno):
            self._propeetario = nombre
        else:
            return False
    
    @property
    def planta(self):
        return self._planta
    
    @planta.setter
    def planta(self, especie):
        if isinstance(especie, Plant):
            self._planta = especie
        else:
            return False
