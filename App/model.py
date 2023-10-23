"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """
import time
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf
import time

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    catalog = {
        "results" : None,
        "scorer" : None,
        "shootouts" :None,
        "tournaments" :None,
        "player" :None,
        "team": None
    }
    catalog["results"] =  mp.newMap(1759,
                            maptype="CHAINING",
                            loadfactor = 8)

    catalog["scorer"] =  mp.newMap(800,
                            maptype="CHAINING",
                            loadfactor = 8)
    
    catalog["shootouts"] =  mp.newMap(17,
                            maptype="CHAINING",
                            loadfactor = 8)
    
    catalog["team"] = mp.newMap(80,
                            maptype="CHAINING",
                            loadfactor = 8)
    catalog["player"] = mp.newMap(80,
                            maptype="CHAINING",
                            loadfactor = 8)
    
    catalog["tournaments"] = mp.newMap(80,
                            maptype="CHAINING",
                            loadfactor = 8)
    return  catalog
# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass

def add_results(catalog, dato, idunica):
    results = catalog["results"]
    
    exitsResults =  mp.contains(results,idunica)
    if exitsResults == False:
        mp.put(results,idunica,dato)

def add_scorer(catalog, dato, idunica ):
    scorer = catalog["scorer"]
    exitsscorer =  mp.contains(scorer,idunica)
    if exitsscorer == False:
        mp.put(scorer,idunica,dato)

def add_shootouts(catalog, dato, idunica ):
    shootouts = catalog["shootouts"]
    exitsshootouts =  mp.contains(shootouts,idunica)
    if exitsshootouts == False:
        mp.put(shootouts,idunica,dato)

# Funciones para creacion de datos

def new_Team():
    team = {
        "datos_home" : None,
        "datos_away" : None
    }
    team["datos_home"] =  lt.newList("ARRAY_LIST")
    team["datos_away"] =  lt.newList("ARRAY_LIST")

    return team

def addTeam(catalog,name,dato,estatus):
    teams =  catalog["team"]
    existteam =  mp.contains(teams,name)
    if existteam:
        entry = mp.get(teams,name)
        team = me.getValue(entry)
    else:
        team = new_Team()
        mp.put(teams,name,team)
    if estatus == "home":
        lt.addLast(team["datos_home"],dato)
    else:
        lt.addLast(team["datos_away"],dato)


def new_Player():
    player = {
        "datos" : None
    }
    player["datos"] =  lt.newList("ARRAY_LIST")

    return player

def addPlayer(catalog,name,dato):
    Players =  catalog["player"]
    existPlayer =  mp.contains(Players,name)
    if existPlayer:
        entry = mp.get(Players,name)
        player = me.getValue(entry)
    else:
        player = new_Player()
        mp.put(Players,name,player)
    lt.addLast(player["datos"],dato)

def new_tournament():
    tournaments = {
        "datos" : None
    }
    tournaments["datos"] =  lt.newList("ARRAY_LIST")

    return tournaments

def addtournament(catalog,name,dato):
    tournaments =  catalog["tournaments"]
    existtournaments =  mp.contains(tournaments,name)
    if existtournaments:
        entry = mp.get(tournaments,name)
        tournament = me.getValue(entry)
    else:
        tournament = new_tournament()
        mp.put(tournaments,name,tournament)
    lt.addLast(tournament["datos"],dato)

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    pass


def req_1(data_structs, team, home):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    teams =  data_structs["team"]
    y = me.getValue(mp.get(teams,team))

    x = "datos_home"
    if home  == "away":
        x = "datos_away"
    nl =  lt.newList("ARRAY_LIST")
    for i in y[x]["elements"]:
        lt.addLast(nl,i)
    return merg.sort(nl,compare_dates_inter)
    

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs, name, fecha_ini, fecha_fin):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    torneos = data_structs["model"]["tournaments"]
    penales = data_structs["model"]["shootouts"]
    fecha_inicio = time.strptime(fecha_ini, "%Y-%m-%d")
    fecha_final = time.strptime(fecha_fin, "%Y-%m-%d")
    t = me.getValue(mp.get(torneos, name))
    torneo = t["datos"]["elements"]
    cant_torn = mp.keySet(torneos)["size"]
    matches = 0
    countries = []
    cities = []
    shootout = 0
    nl = lt.newList("ARRAY_LIST")
    for i in torneo:
        fecha_actual = time.strptime(i["date"], "%Y-%m-%d")
        if fecha_actual > fecha_inicio and fecha_actual < fecha_final:
            x = {}
            matches += 1
            if not(i["country"]) in countries:
                countries.append(i["country"])
            if not(i["city"]) in cities:
                cities.append(i["city"])
            x["date"] = i["date"]
            x["tournament"] = i["tournament"]
            x["country"] = i["country"]
            x["home_team"] = i["home_team"]
            x["away_team"] = i["away_team"]
            x["home_score"] = i["home_score"]
            x["away_score"] = i["away_score"]
            x["winner"] = "Unavailable"
            idunica = str( i["date"]+ "-" + i["home_team"] + "-" + i["away_team"])
            if mp.contains(penales, idunica):
                shootout += 1
                p = me.getValue(mp.get(penales, idunica))
                x["winner"] = p["winner"]
            lt.addLast(nl, x)
    map4 = mp.newMap()
    mp.put(map4, "values", nl)
    mp.put(map4, "tournaments", cant_torn)
    mp.put(map4, "matches", matches)
    mp.put(map4, "countries", len(countries))
    mp.put(map4, "cities", len(cities))
    mp.put(map4, "shootout", shootout)
    return map4
            
    
    


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare1(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if data_1["date"] < data_2["date"]:
        return 0
    else:
        return 1

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass

def compare_dates_inter(data_1,  data_2):
    x = (data_1["date"])
    y = (data_2["date"])
    first = time.strptime(x, "%Y-%m-%d")
    second = time.strptime(y, "%Y-%m-%d")
    return first < second
def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
