import Constantes
import Utils

import csv
from io import StringIO
import requests

# Base datos -------------------------------------------------------------------

"""Devuelve una lista de Strings de las clases de la fecha indicada"""
def getSubjectByDate(fecha):
    f=open(Constantes.FILE_NAME, 'r')
    n = ""
    result = []
    for clase in f.readlines()[1:]:
        n = clase.split(",")
        if(n[FECHA_POS].strip().__eq__(fecha)):
            result.append(clase)

    f.close()

    if(len(result)==0):
        raise ValueError()

    return result


def saveTextToFile(fileName, txt):
    f=open(fileName, 'w')

    for l in txt:
        if(len(l)>2):
            f.write(l+"\n")

    f.close()

def hasToUpdateDB():
    try:
        f=open(Constantes.FILE_NAME, 'r')
        lastUpdate = f.readline().strip()
        f.close()
    except FileNotFoundError:
        return(True)

    return(lastUpdate!=Constantes.todayDate)

def updateDB():
    Utils.say("Updating dataBase...")
    urlCSV = Utils.processVistaURL(Constantes.CSV)
    req = requests.get(urlCSV, verify=False)
    data = req.text

    s = []
    for l in str(data).split("\n"):
        s.append(l)
    s = s[1:]
    s.insert(0, Constantes.todayDate)
    saveTextToFile(Constantes.FILE_NAME, s)
    Utils.say("All Up-To-Date")



