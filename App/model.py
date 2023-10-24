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
from tabulate import tabulate
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
    catalog["player_names"] = lt.newList("ARRAY_LIST")

    catalog["teams_names"] = lt.newList("ARRAY_LIST")
    
    catalog["tournaments"] = mp.newMap(80,
                            maptype="CHAINING",
                            loadfactor = 8)
                            
    return  catalog
# Funciones para agregar informacion al modelo
def data_sizel(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    return lt.size(data_structs) 
def sublista(data_structs, pos_i, num):
    s =  lt.subList(data_structs, pos_i, num)
    return s



def first_last3(data_structs):
    primeros = sublista(data_structs,1,3)
    ultimos = sublista(data_structs,data_sizel(data_structs)-2,3)
    for i in lt.iterator(ultimos):
        lt.addLast(primeros,i)
    return primeros

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


def new_Scorer():
    games = {
        "datos" : None
    }
    games["datos"] =  lt.newList("ARRAY_LIST")
    return games


def add_scorer(catalog, dato, idunica ):
    scorer = catalog["scorer"]
    exitsscorer =  mp.contains(scorer,idunica)
    if exitsscorer:
        entry = mp.get(scorer,idunica)
        game = me.getValue(entry)
    else:
        game = new_Scorer()
        mp.put(scorer,idunica,game)
    lt.addLast(game["datos"],dato)


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

def add_player_names(lista,name):
    if lt.isPresent(lista,name) == 0:
        lt.addLast(lista,name)
def add_team_names(lista,name):
    if lt.isPresent(lista,name) == 0:
        lt.addLast(lista,name)

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
    j = len(y["datos_home"]["elements"])+  len(y["datos_away"]["elements"])
    return merg.sort(nl,compare_dates_inter_mayor), j
    

def req_2(data_structs, name):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    players = data_structs["player"]
    player  =  me.getValue(mp.get(players,name)) 
    nl =  lt.newList("ARRAY_LIST")
    for i in player["datos"]["elements"]:
        lt.addLast(nl,i)
    return merg.sort(nl,compare_dates_inter_menor)

def req_3(data_structs,team,date_i,date_f):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    scorer =  data_structs["scorer"]
    teams =  data_structs["team"]
    y = me.getValue(mp.get(teams,team))
    nl =  lt.newList("ARRAY_LIST")
    first = time.strptime(date_i, "%Y-%m-%d")
    second = time.strptime(date_f, "%Y-%m-%d")
    nl = complement_req3("datos_home",first,second,scorer,y,nl)
    nl = complement_req3("datos_away",first,second,scorer,y,nl)
    o =  merg.sort(nl,compare_dates_inter_menor)
    return o
def complement_req3(pos,first,second,scorer,y,nl):
    for i in y[pos]["elements"]:
        date_actual =  time.strptime(i["date"], "%Y-%m-%d")
        if date_actual > first and date_actual < second:
            idunica =  i["date"]+ "-" + i["home_team"] + "-" + i["away_team"]
            d = {}
            d["date"] = i["date"]
            d["home_score"] = i["home_score"]
            d["away_score"] = i["away_score"]
            d["home_team"] = i["home_team"]
            d["away_team"] = i["away_team"]
            d["country"] = i["country"]
            d["city"] = i["city"]
            d["tournament"] = i["tournament"]
            d["penalty"] = "Unknown"
            d["own_goal"] = "Unknown"
            exitsscorer =  mp.contains(scorer,idunica)
            if exitsscorer:
                valores_scorer = me.getValue(mp.get(scorer,idunica))
                lista1=(valores_scorer["datos"]["elements"])[0]
                if lista1["penalty"] != "":
                    d["penalty"] =  lista1["penalty"]
                if lista1["own_goal"] != "":
                    d["own_goal"] =  lista1["own_goal"]         
            lt.addLast(nl,d)
    return nl
def req_4(data_structs):
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
            
    
    


def req_5(data_structs, name, fecha_ini, fecha_fin):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass



def new_Country_Player():
    team_country = {
        "datos" : None
    }
    team_country["datos"] =  lt.newList("ARRAY_LIST")
    team_country["jugadores"] =  lt.newList("ARRAY_LIST")
    team_country["results"] =  lt.newList("ARRAY_LIST")

    return team_country

def new_bests_Player():
    team_country = {
        "jugadores" : None
    }

    team_country["jugadores"] =  lt.newList("ARRAY_LIST")

    return team_country

def req_6(data_structs, torneo = "FIFA World Cup qualification", anio = "2021"):
    """
    Función que soluciona el requerimiento 6
    """
    
    # TODO: Realizar el requerimiento 6
    torneos =  data_structs["tournaments"]
    scorer = data_structs["scorer"]
    results = data_structs["results"]
    teams = data_structs["team"]
    team_names = data_structs["teams_names"]
    player_names = data_structs["player_names"]
    torneom = me.getValue(mp.get(torneos,torneo))
    d={}
    map1 = mp.newMap()  
    map2 = mp.newMap()  
    map3 = mp.newMap()  
    map4 = mp.newMap()  
    d["teams"] =  map1
    map1= d["teams"]
    nl = lt.newList("ARRAY_LIST")
    nl1 = lt.newList("ARRAY_LIST")
    for i in torneom["datos"]["elements"]:
       anioi = i["date"]
       anioi = anioi[0:4]
       if anio == anioi:
            lt.addLast(nl,i)
            idunica =  str(i["date"]+ "-" + i["home_team"] + "-" + i["away_team"])
        
            exitsResults =  mp.contains(scorer,idunica)
            exitsresults =  mp.contains(results,idunica)
            if exitsresults:
                valores_results = me.getValue(mp.get(results,idunica))
                datos1= valores_results
                pais =datos1["home_team"]
                existteam1 =  mp.contains(map1,pais)
                if existteam1:
                    entry = mp.get(map1,pais)
                    team = me.getValue(entry)
                else:
                    team = new_Country_Player()
                    mp.put(map1,pais,team)
                lt.addLast(team["results"],datos1)
                pais =datos1["away_team"]
                existteam1 =  mp.contains(map1,pais)
                if existteam1:
                    entry = mp.get(map1,pais)
                    team = me.getValue(entry)
                else:
                    team = new_Country_Player()
                    mp.put(map1,pais,team)
                lt.addLast(team["results"],datos1)
            if exitsResults:
                valores_results = me.getValue(mp.get(scorer,idunica))
                pais2= valores_results["datos"]["elements"]
                for h in pais2:
                    pais = h["team"]
                    nombre = h["scorer"]
                    existteam =  mp.contains(map1,pais)
                    if existteam:
                        entry = mp.get(map1,pais)
                        team = me.getValue(entry)
                    else:
                        team = new_Country_Player()
                        mp.put(map1,pais,team)
                    lt.addLast(team["datos"],h)
                    lt.addLast(team["jugadores"],nombre)
    
    for i in lt.iterator(team_names):
        exitsi =  mp.contains(map1,i)
        if exitsi:
            nj =  lt.newList("ARRAY_LIST")
            pais_datos  = me.getValue(mp.get(map1,i))
            datos  = pais_datos["datos"]["elements"]
            jugadores  = pais_datos["jugadores"]["elements"]
            r  = pais_datos["results"]["elements"]
            dr =  {}
            for results in r:
                if dr == {}:
                    dr["team"] = ""
                    dr["total_points"] = 0
                    dr["goal_difference"] = 0
                    dr["penalty_points"] = 0
                    dr["matches"] = 0
                    dr["own_goals_points"] = 0
                    dr["wins"] = 0
                    dr["draws"] = 0
                    dr["losses"] = 0
                    dr["goals_for"] = 0
                    dr["goals_against"] = 0
                    dr["top_scorer"] = {}
                    if results["home_team"] == i:
                        dr["team"] = results["home_team"]
                        dr["matches"] =  int(dr["matches"]) + 1

                        if int(results["home_score"]) > int(results["away_score"]):
                            dr["total_points"] =  int(dr["total_points"]) + 3
                            dr["wins"] =  int(dr["wins"]) + 1
                        if int(results["home_score"]) == int(results["away_score"]):
                            dr["total_points"] =  int(dr["total_points"]) + 1
                            dr["draws"] =  int(dr["draws"]) + 1
                        else:
                            dr["losses"] =  int(dr["losses"]) + 1
                        dr["goals_for"] = int( dr["goals_for"] ) + int(results["home_score"])
                        dr["goals_against"] = int( dr["goals_against"] ) + int(results["away_score"])
                        dr["goal_difference"] =  int(dr["goal_difference"]) + (int(results["home_score"]) - int(results["away_score"]))
                        dr["goals_for"] =  dr["goals_for"] + int(results["home_score"])
                        idunica1 =  str(results["date"]+ "-" + results["home_team"] + "-" + results["away_team"])

                        exitsResults =  mp.contains(scorer,idunica1)
                        if exitsResults:
                            valores_results = me.getValue(mp.get(scorer,idunica1))
                            pais2= valores_results["datos"]["elements"]
                            for h in pais2:
                                pais = h["team"]
                                if pais == i:
                                    if h["penalty"] == "True":
                                        dr["penalty_points"] = int(dr["penalty_points"]) + 1
                                    if h["own_goal"] == "True":
                                        dr["own_goals_points"] = int(dr["own_goals_points"]) + 1
                    if results["away_team"] == i:
                        dr["matches"] =  int(dr["matches"]) + 1
                        dr["team"] = results["away_team"]
                        if int(results["away_score"]) > int(results["home_score"]):
                            dr["total_points"] =  int(dr["total_points"]) + 3
                            dr["wins"] =  int(dr["wins"]) + 1
                        if int(results["away_score"]) == int(results["home_score"]):
                            dr["total_points"] =  int(dr["total_points"]) + 1
                            dr["draws"] =  int(dr["draws"]) + 1
                        else:
                            dr["losses"] =  int(dr["losses"]) + 1
                        dr["goals_for"] = int( dr["goals_for"] ) + int(results["away_score"])
                        dr["goals_against"] = int( dr["goals_against"] ) + int(results["home_score"])
                        dr["goal_difference"] =  int(dr["goal_difference"]) + (int(results["away_score"]) - int(results["home_score"]))
                        dr["goals_for"] =  dr["goals_for"] + int(results["away_score"])
                        idunica1 =  str(results["date"]+ "-" + results["home_team"] + "-" + results["away_team"])

                        exitsResults =  mp.contains(scorer,idunica1)
                        
                        if exitsResults:
                            valores_results = me.getValue(mp.get(scorer,idunica1))
                            pais2= valores_results["datos"]["elements"]
                            for h in pais2:
                                pais = h["team"]
                                if pais == i:
                                    if h["penalty"] == "True":
                                        dr["penalty_points"] = int(dr["penalty_points"]) + 1
                                    if h["own_goal"] == "True":
                                        dr["own_goals_points"] = int(dr["own_goals_points"]) + 1
            mp.put(map4,i,dr)
                
            for j in jugadores:      
                d  = {}
                d["scorer"] =  j
                d["goals"] = 0
                d["matches"] = 0
                d["avg_time"] = 0
                d["minute"] = 0
                for z in datos:
                    if z["scorer"] == j:        
                        exits_jugadormayor = mp.contains(map3,j)
                        if exits_jugadormayor:
                            jugador_map =  me.getValue(mp.get(map3,j))
                            if jugador_map["penalty"] != "True":
                                d["goals"] = int(jugador_map["goals"]) + 1
                            d["matches"] = int(jugador_map["matches"]) + 1
                            d["minute"] = int(jugador_map["minute"]) + int(jugador_map["minute"])
                            d["avg_time"] = float(d["minute"])/float(d["matches"])
                        else:

                            if z["penalty"] != "True":
                                d["goals"] =  1
                            d["matches"] =  1
                            d["minute"] = float(z["minute"])
                            d["avg_time"] = float(d["minute"])/float(d["matches"])    
                lt.addLast(nj,d)       
            mp.put(map3,i,nj)
        exits0 =  mp.contains(map3,i)
        if exits0: 
            determinar_mayor =  me.getValue(mp.get(map3,i))
            d  = {}
            d["scorer"] = ""
            d["goals"] = 0
            d["matches"] = 0
            d["avg_time"] = 0
            d["minute"] = 0 
            for p in determinar_mayor["elements"]:
                if d == {}:
                    d = p
                if d["goals"] < p["goals"]:
                    d = p
                    if d["matches"] > p["matches"]:
                        d = p
            mp.put(map2,i,d)
        exitsmap4 = mp.contains(map4,i)
        if exitsmap4:
            

            valuemap = me.getValue(mp.get(map4,i))

            dicfinal = valuemap
            dicfinal["top_scorer"] = {}
            dicfinal["top_scorer"]["scorer"] = "Unavailable"
            dicfinal["top_scorer"]["goals"] = 0
            dicfinal["top_scorer"]["matches"] = 0
            dicfinal["top_scorer"]["avg_time"] = 0
            dicfinal["top_scorer"]["minute"] = 0 
            exitsmap2 = mp.contains(map2,i)
            if exitsmap2:
                valueplayer = me.getValue(mp.get(map2,i))
                dicfinal["top_scorer"] = valueplayer
            lt.addLast(nl1,valuemap)
  
        
    return nl1


def req_7(data_structs, name, tamanio):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    # Revisar, ya que estoy bugeado
    torneos = data_structs["model"]["tournaments"]
    scorers = data_structs["model"]["scorer"]
    cant_torn = mp.keySet(torneos)["size"]
    t = me.getValue(mp.get(torneos, name))
    torneo = t["datos"]["elements"]
    golea = {}
    matches = 0
    penalties = 0
    autogoals = 0  
    goals = 0
    for i in torneo:
        idunica =  str( r["date"]+ "-" + r["home_team"] + "-" + r["away_team"]+ "-" + r["minute"])
        goal = me.getValue(mp.get(scorers,idunica))
        if not(goal["scorer"]) in golea:
            golea[goal["scorer"]] = {}
            golea[goal["scorer"]]["total_points"] = 0
            golea[goal["scorer"]]["total_goals"] = 0
            golea[goal["scorer"]]["penalty_goals"] = 0
            golea[goal["scorer"]]["own_goals"] = 0
            golea[goal["scorer"]]["sum_time"] = 0
            golea[goal["scorer"]]["avg_time [min]"] = 0
            golea[goal["scorer"]]["scored_in_wins"] = 0
            golea[goal["scorer"]]["scored_in_losses"] = 0
            golea[goal["scorer"]]["scored_in_draws"] = 0
            golea[goal["scorer"]]["last_goal"] = {}
        # Suma de goles, penalty, autogoles y puntos
        golea[goal["scorer"]]["total_goals"] += 1
        if goal["penalty"] == "True":
            golea[goal["scorer"]]["penalty_goals"] += 1
        if goal["own_goal"] == "True":
            golea[goal["scorer"]]["own_goals"] += 1
        golea[goal["scorer"]]["total_points"] = golea[goal["scorer"]]["total_goals"] + golea[goal["scorer"]]["penalty_goals"] - golea[goal["scorer"]]["own_goals"]
        # Suma y promedio de minutos
        golea[goal["scorer"]]["sum_time"] += goal["minute"]
        golea[goal["scorer"]]["avg_time [min]"] = golea[goal["scorer"]]["sum_time"]/golea[goal["scorer"]]["total_goals"]
        # Goles en wins
        if goal["team"] == goal[""]:
            pass
        idunica =  str( i["date"]+ "-" + i["home_team"] + "-" + i["away_team"])
        goals += int(i["home_score"]) + int(i["away_score"])
        if mp.contains(scorers, idunica):
            goal = me.getValue(mp.get(scorers,idunica))
            goal = goal["datos"]["elements"]
            matches += 1
            for j in goal:
                if not(j["scorer"]) in golea:
                    golea[j["scorer"]] = {}
                    golea[j["scorer"]]["total_points"] = 0
                    golea[j["scorer"]]["total_goals"] = 0
                    golea[j["scorer"]]["penalty_goals"] = 0
                    golea[j["scorer"]]["own_goals"] = 0
                    golea[j["scorer"]]["sum_time"] = 0
                    golea[j["scorer"]]["avg_time [min]"] = 0
                    golea[j["scorer"]]["scored_in_wins"] = 0
                    golea[j["scorer"]]["scored_in_losses"] = 0
                    golea[j["scorer"]]["scored_in_draws"] = 0
                # Suma de goles, penalty, autogoles y puntos
                golea[j["scorer"]]["total_goals"] += 1
                if j["penalty"] == "True":
                    golea[j["scorer"]]["penalty_goals"] += 1
                    penalties += 1
                if j["own_goal"] == "True":
                    golea[j["scorer"]]["own_goals"] += 1
                    autogoals += 1
                golea[j["scorer"]]["total_points"] = golea[j["scorer"]]["total_goals"] + golea[j["scorer"]]["penalty_goals"] - golea[j["scorer"]]["own_goals"]
                # Suma y promedio de minutos
                golea[j["scorer"]]["sum_time"] += float(j["minute"])
                golea[j["scorer"]]["avg_time [min]"] = golea[j["scorer"]]["sum_time"]/golea[j["scorer"]]["total_goals"]
                # Goles en wins
                if j["team"] == j["home_team"] and i["home_score"] > i["away_score"]:
                    golea[j["scorer"]]["scored_in_wins"] +=1
                if j["team"] == j["away_team"] and i["home_score"] < i["away_score"]:
                    golea[j["scorer"]]["scored_in_wins"] +=1
                # Goles en draws
                if j["team"] == j["home_team"] and i["home_score"] == i["away_score"]:
                    golea[j["scorer"]]["scored_in_draws"] +=1
                if j["team"] == j["away_team"] and i["home_score"] == i["away_score"]:
                    golea[j["scorer"]]["scored_in_draws"] +=1
                # Goles en losses
                if j["team"] == j["home_team"] and i["home_score"] < i["away_score"]:
                    golea[j["scorer"]]["scored_in_losses"] +=1
                if j["team"] == j["away_team"] and i["home_score"] > i["away_score"]:
                    golea[j["scorer"]]["scored_in_losses"] +=1
                # Ultimo gol
                golea[j["scorer"]]["last_goal"] = {"date": j["date"], "home_team": j["home_team"], "away_team": j["away_team"], "home_score": i["home_score"], "away_score": i["away_score"], "minute": j["minute"], "penalty": j["penalty"], "own_goal": j["own_goal"]}
    goleadores = list(golea.keys())
    players = len(goleadores)
    valores = list(golea.values())
    npuntos = lt.newList("ARRAY_LIST")
    withnpuntos = 0
    for i in range(len(goleadores)):
        x = {}
        # Filtrar los de N puntos
        if valores[i]["total_points"] == tamanio:
            x["scorer"] = goleadores[i]
            x["total_points"] = valores[i]["total_points"]
            x["total_goals"] = valores[i]["total_goals"]
            x["penalty_goals"] = valores[i]["penalty_goals"]
            x["own_goals"] = valores[i]["own_goals"]
            x["avg_time [min]"] = valores[i]["avg_time [min]"]
            x["scored_in_wins"] = valores[i]["scored_in_wins"]
            x["scored_in_losses"] = valores[i]["scored_in_losses"]
            x["scored_in_draws"] = valores[i]["scored_in_draws"]
            lg = lt.newList("ARRAY_LIST")
            lt.addLast(lg, valores[i]["last_goal"])
            x["last_goal"] = tabulate(lg["elements"], headers = "keys" , tablefmt='grid')
            lt.addLast(npuntos, x)
            withnpuntos += 1
    map7 = mp.newMap()
    mp.put(map7, "values", npuntos)
    mp.put(map7, "players", players)
    mp.put(map7, "goals", goals)
    mp.put(map7, "tournaments", cant_torn)
    mp.put(map7, "penalties", penalties)
    mp.put(map7, "autogoals", autogoals)
    mp.put(map7, "matches", matches)
    mp.put(map7, "n-points", withnpuntos)
    return map7
        

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
def compare_dates_inter_menor(data_1,  data_2):
    x = (data_1["date"])
    y = (data_2["date"])
    first = time.strptime(x, "%Y-%m-%d")
    second = time.strptime(y, "%Y-%m-%d")
    return first < second

def compare_dates_inter_mayor(data_1,  data_2):
    x = (data_1["date"])
    y = (data_2["date"])
    first = time.strptime(x, "%Y-%m-%d")
    second = time.strptime(y, "%Y-%m-%d")
    return first > second

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
