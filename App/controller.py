﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import tracemalloc
import time
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
    """
    Crea una instancia del modelo
    """
      
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control
    #TODO: Llamar la función del modelo que crea las estructuras de datos
    


# Funciones para la carga de datos

def load_data(control,memflag=True):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = getTime()

    # inicializa el proceso para medir memoria
    if memflag is True:
        tracemalloc.start()
        start_memory = getMemory()
    load_scorers(control)
    load_results(control)
    load_shootouts(control)
    stop_time = getTime()
    # calculando la diferencia en tiempo
    delta_time = deltaTime(stop_time, start_time)

    # finaliza el proceso para medir memoria
    if memflag is True:
        stop_memory = getMemory()
        tracemalloc.stop()
        # calcula la diferencia de memoria
        delta_memory = deltaMemory(stop_memory, start_memory)
        # respuesta con los datos de tiempo y memoria
        return delta_time, delta_memory

    else:
        # respuesta sin medir memoria
        return delta_time

def load_scorers(control):
    scorer_file  = cf.data_dir + 'football/goalscorers-utf8-small.csv'
    input_file = csv.DictReader(open(scorer_file, encoding='utf-8'))
    for r in input_file:
        model.adlista(control,"scorer1",r)
        idunica =  str( r["date"]+ "-" + r["home_team"] + "-" + r["away_team"])
        model.add_scorer(control["model"],r,idunica)
        model.addPlayer(control["model"],r["scorer"],r)
        model.add_player_names(control["model"]["player_names"],r["scorer"])
    control["model"]["scorer1"] = model.sortLista(control["model"]["scorer1"])


def load_results(control):
    scorer_file  = cf.data_dir + 'football/results-utf8-small.csv'
    input_file = csv.DictReader(open(scorer_file, encoding='utf-8'))
    for r in input_file:
        model.adlista(control,"results1",r)
        idunica =  str( r["date"]+ "-" + r["home_team"] + "-" + r["away_team"] )
        model.add_results(control["model"],r,idunica) 
        model.addTeam(control["model"],r["home_team"],r,"home")
        model.addTeam(control["model"],r["away_team"],r,"away")
        model.addtournament(control["model"],r["tournament"],r)
        model.add_team_names(control["model"]["teams_names"],r["home_team"])
        model.add_team_names(control["model"]["teams_names"],r["away_team"])
    control["model"]["results1"] = model.sortLista(control["model"]["results1"])
    
        
def load_shootouts(control):
    scorer_file  = cf.data_dir + 'football/shootouts-utf8-small.csv'
    input_file = csv.DictReader(open(scorer_file, encoding='utf-8'))
    for r in input_file:
        model.adlista(control,"shootouts1",r)
        idunica =  str( r["date"]+ "-" + r["home_team"] + "-" + r["away_team"])
        model.add_shootouts(control["model"],r,idunica)        
    control["model"]["shootouts1"] = model.sortLista(control["model"]["shootouts1"])
    
# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass
def sizedtos(control,posi):
    pos = control["model"]
    return model.data_size(pos[posi])

def sizedtosl(control):
    return model.data_sizel(control)

def primeros_ultimos(control):
    return model.first_last3(control) 

def req_1(control,team, home,n):
    """
    Retorna el resultado del requerimiento 1
    """

    # TODO: Modificar el requerimiento 
    
  
    rq1model, j = model.req_1(control["model"],team, home)

    size= model.data_sizel(rq1model)
    size_i = size
    if size > n:
        size = n
        rq1model =  model.sublista(rq1model,1,size)
    
    if size > 6:
        rq1model =  model.first_last3(rq1model)
    return  rq1model, size ,size_i , j

   


def req_2(control,name,n):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    rq2model = model.req_2(control["model"],name)

    size= model.data_sizel(rq2model)
    size_i = size
    if size > n:
        size = n
        rq2model =  model.sublista(rq2model,1,size)
    
    if size > 6:
        rq1model =  model.first_last3(rq1model)
    return  rq2model, size ,size_i


def req_3(control, team, date_i, date_f):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el reqtart = get_time()
    dtos =  model.req_3(control,date_i, date_f , team)
    # TODO: Modificar el requerimiento 3
    map3 = model.req_3(control["model"], team, date_i, date_f)
    return map3



def req_4(control, name, fecha_ini, fecha_fin):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    map4 = model.req_4(control, name, fecha_ini, fecha_fin)
    return map4


def req_5(control, name, fecha_ini, fecha_fin):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    map5 = model.req_5(control, name, fecha_ini, fecha_fin)
    return map5

def req_6(control, torneo,anio,n):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    rq6model = model.req_6(control, torneo, anio)

    size= model.data_sizel(rq6model)
    size_i = size
    if size > n:
        size = n
        rq6model =  model.sublista(rq6model,1,size)
    
    if size > 6:
        rq6model =  model.first_last3(rq6model)
    return  rq6model, size ,size_i

def req_7(control, name, tamanio):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    return model.req_7(control, name, tamanio)


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def deltaTime(end, start):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed


# Funciones para medir la memoria utilizada


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()

def deltaMemory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory

