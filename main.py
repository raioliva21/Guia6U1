#!/usr/bin/env python3
from alumno import Alumno
from garden import Garden
from vaso import Vaso
from hierba import Hierba
from rabano import Rabano
from trebol import Trebol
from violeta import Violeta
import random 

""" funcion asociada a acciones dependientes de decision """
def decision_usuario(decision, garden, filas, columnas):

    if decision == '0':
        exit()
    continuar_busqueda = "S"
    while continuar_busqueda == 'S':
        garden.get_vista(filas, columnas)
        print("LISTA DE ESTUDIANTES REGISTRADOS")
        garden.get_lista_alumnos()
        if decision == '1':
            print("Ingrese nombre de estudiante\
 para averiguar plantas que le pertenecen. ")
            nombre_alumno = input("> ")
            garden.planta(nombre_alumno)
        elif decision == '2':
            print("{0} filas de {1} columnas de vasos con plantas"\
                .format(filas, columnas))
            print("A continuacion, ingrese numero de\
 fila y columna de vaso(planta) a consultar. Valor min.=1")
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            print(f"El vaso(planta) de pos({fila},{columna})\
 pertenece a")
            print(garden.vaso[fila-1][columna-1].propeetario)
        else:
            print("Error, opcion no valida")
            continuar_busqueda = None
        print("¿Desea continuar con busqueda?S/n")
        x = input(">")
        continuar_busqueda = x.capitalize()

""" funcion principal """
def main():

    nombre_alumnos = " Alicia, Marit, Pepito, David,\
                        Eva, Lucia, Rocio, Andres, Jose,\
                        Belen, Sergio y Larry"

    """ manejo de string 'nombre_alumnos' """
    nombre_alumnos = nombre_alumnos.split(",")
    if " y " in nombre_alumnos[-1]:
        x = nombre_alumnos[-1].split(" y ")
        nombre_alumnos[-1] = x[0]
        nombre_alumnos.append(x[1])
    for i in range(0, len(nombre_alumnos)):
        nombre_alumnos[i] = nombre_alumnos[i].strip()

    # orden alfabetico de nombres de alumnos
    nombre_alumnos.sort()

    """ creacion lista que abarca objetos de clase alumno """
    alumnos = []
    for i in nombre_alumnos:
        # creacion objetos tipo alumno
        # clase alumno recibe nombre de alumno como argumento
        alumnos.append(Alumno(i))
    
    # lista que contiene objetos heredados de clase 'Plant'
    plantas = [Hierba(), Rabano(), Trebol(), Violeta()]
    
    """se asigna valores a 'planta' de objetos clase alumno"""
    # planta es atributo de objeto tipo alumno
    for i in alumnos:
        for j in range(0,4):
            # metodo random para asignar valor
            planta_seleccionada = random.choice(plantas)
            # se asigna valor a atributo 'planta'
            i.planta = planta_seleccionada
    
    """ creacion matriz 2D para objetos tipo vaso """
    filas, columnas = (2, len(alumnos)*2)
    vaso =[]
    for i in range(filas):
        columna = []
        for j in range(columnas):
            columna.append(0)
        vaso.append(columna)
    n = 0
    """ asignacion de valores clase 'vaso' a elementos de 
    lista vaso."""
    for i in alumnos:
        for j in range(0,4):
            if j < 2:
                # fila 0
                vaso[0][n] = Vaso(i.nombre, i.planta[j])
            else:
                # fila 1
                if j == 2:
                    n = n - 2
                vaso[1][n] = Vaso(i.nombre, i.planta[j])
            n = n + 1

        print("\n")

    """ creacion objeto 'garden' que agrupara acciones """
    garden = Garden(vaso, alumnos)
    # muestra vista de atributos de objeto garden
    # muestra representacion de atributos vasos y ventanas
    garden.get_vista(filas, columnas)
    """ menu de interaccion con usuario """
    while decision_usuario != '0':
        print("MENU")
        print("<1> para averiguar plantas de alumno \
determinado.")
        print("<2> para averiguar a que alumno \
pertenece planta determinada.")
        print("<0> para acabar programa.")
        decision = input(">")
        # dirigue a funcion
        decision_usuario(decision, garden, filas, columnas)

if __name__ == "__main__":
    main()
