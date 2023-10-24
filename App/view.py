"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    return controller.new_controller()


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos

    controller.load_data(control)




def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    print("Req No. 1 Input".center(130,"="))

    n =  int(input("Number of matches: "))
    team_name =  input("Team name: ")
    tipolocal =  input("Team condition: ")

    print("Req No. 1 Results".center(130,"="))
    l1,l2, l3=controller.req_1(control,team_name,tipolocal,n)
    print(("Total matches found "+ str(l3)).center(100))
    print(("Selecting "+ str(l2) + " matches...").center(100))
    if l3 > 6:
        print("Resultrs struct has more than 6 records...")
    else:
        print("Resultrs struct has less than 6 records...")
    print(tabulate(l1["elements"], headers = "keys" , tablefmt='grid'))
    print(l2)
  

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control, name, fecha_ini, fecha_fin):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    map4 = controller.req_4(control, name, fecha_ini, fecha_fin)
    print(me.getValue(mp.get(map4,"tournaments")))
    print(me.getValue(mp.get(map4,"matches")))
    print(me.getValue(mp.get(map4,"countries")))
    print(me.getValue(mp.get(map4,"cities")))
    print(me.getValue(mp.get(map4,"shootout")))
    print(tabulate(me.getValue(mp.get(map4,"values"))["elements"], headers = "keys" , tablefmt='grid'))


def print_req_5(control, name, fecha_ini, fecha_fin):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    map5 = controller.req_5(control, name, fecha_ini, fecha_fin)
    print(me.getValue(mp.get(map5,"players")))
    print(me.getValue(mp.get(map5,"goals")))
    print(me.getValue(mp.get(map5,"tournaments")))
    print(me.getValue(mp.get(map5,"penalties")))
    print(me.getValue(mp.get(map5,"autogoals")))
    print(tabulate(me.getValue(mp.get(map5,"values"))["elements"], headers = "keys" , tablefmt='grid'))


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            print(data)
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control, "Copa América", "1955-06-01", "2022-06-30")

        elif int(inputs) == 6:
            print_req_5(control, "Ali Daei", "1999-03-25", "2021-11-23")

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
