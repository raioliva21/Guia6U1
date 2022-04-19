#!/usr/bin/env python3
from operator import truediv

class Garden():

    def __init__(self, vaso, alumnos) -> None:
        self._vaso = vaso #lista de vasos
        self._alumnos = alumnos #lista de alumnos
        # atributo publico
        self.ventana = "[ventana]"
        pass

    def get_vista(self, filas, columnas):
        print(self.ventana*3)
        for fila in range(0,filas):
            for columna in range(0,columnas):
                if columna == 0:
                    print(" ", end="")
                print(self._vaso[fila][columna].planta.letra,\
                    end="")
            print("")
    
    def get_lista_alumnos(self):
        for alumno in self._alumnos:
            print(alumno.nombre)

    def planta(self, nombre_estudiante):
        coincidencia = None
        if isinstance (nombre_estudiante, str):
            nombre_estudiante = nombre_estudiante.capitalize()
            #nombre_estudiante.capitalize()
            for alumno in self._alumnos:
                if alumno.nombre == nombre_estudiante:
                    coincidencia = True
                    return alumno.muestra_plantas()
                else:
                    pass
            if coincidencia is not True:
                print("Error, dato ingresado no ha", end=" ")
                print("sido encontrado en el", end= " ")
                print("registro de alumnos.")
        else:
            print("Error, dato ingresado no es tipo string.")
    
    @property
    def vaso(self):
        return self._vaso

    @property
    def alumnos(self):
        return self._alumnos
    