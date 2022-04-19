#!/usr/bin/env python3
from plant import Plant

class Alumno():

    def __init__(self, nombre) -> None:
        self._nombre = nombre #nombre de alumno
        self._planta = [] #lista de plantas
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self._nombre = nombre
        else:
            return False
    
    @property
    def planta(self):
        return self._planta
    
    @planta.setter
    def planta(self, planta):
        if isinstance(planta, Plant):
            self._planta.append(planta)
        else:
            print("Argumento no corresponde a clase 'Plant'.")
            return False

    """ muestra elementos de lista planta por separado"""    
    def muestra_plantas(self):
        for planta in self._planta:
            print(planta.letra)



