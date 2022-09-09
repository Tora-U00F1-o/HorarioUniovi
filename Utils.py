import Constantes

import time

# INPUT ------------------------------------------------------------------------

"""Pide lo que sea por consola"""
def ask(mensaje):
    return input(str(mensaje))

"""Pide por consola un Entero"""
def askInt(mensaje):
    while(True):
        try:
            return int(ask(mensaje))
        except ValueError:
            continue

# OUTPUT -----------------------------------------------------------------------

"""Imprime por consola el mensaje"""
def say(mensaje):
    print(mensaje)

# Dates stuff ------------------------------------------------------------------

def getTodayDate():
    day = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")

    todayDate = day+"/"+month+"/"+year
    return todayDate


def processMonthKey(dayWithKey):
    dayWithKey = dayWithKey.strip()
    if(dayWithKey[0] == '-'):
        return dayWithKey[1:], -1

    elif (dayWithKey[0] == '+'):
        return dayWithKey[1:], +1

    else: return dayWithKey, 0


def processDate(dateToProcess):
    dateProcessed = getTodayDate().split("/")
    dateArray = dateToProcess.split("/")

    ## permite hacer "[+|-]?numDia"
    ## ej: se puede ver el dia 4 del mes anterior con "-4" y el del siguiente "+4"
    dateArray[0], monthKey = processMonthKey(dateArray[0])
    if(monthKey != 0):
        dateArray.append(str(int(dateProcessed[1])+monthKey))

    for i in range(len(dateArray)):
        string = dateArray[i].strip()
        if(len(string) == 1):
            string = "0"+string
        dateProcessed[i] = string

    return dateProcessed[0]+"/"+dateProcessed[1]+"/"+dateProcessed[2]

# URL --------------------------------------------------------------------------

"""Devuelve la URL con la vista indicada por parametro"""
## En la URL hay un parametro qe es vista, es el primer parametro del http
##      \--> " ... php?vista=csv&y=21 ..." está separada por "&" del resto de
##              parametros
## Entonces buscamos el substring de "vista=xxx&" y sustituimos el valor "xxx"
def processVistaURL(type):
    return processVistaURL(Constantes.URL, type)
def processVistaURL(url, type):
    strToSearch = 'vista='
    indexStart = url.find(strToSearch) + len(strToSearch)
    strToSearch = '&'
    indexEnd = url.find(strToSearch)

    newURL = url[:indexStart] + type + url[indexEnd:]
    return newURL