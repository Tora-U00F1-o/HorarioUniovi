import WebUtils
import Utils
import Constantes
import ExplorerUtils
import InterfazUtils

import csv
from io import StringIO
import requests



arch = Constantes.DATA_DIRECTORY+"___p.txt"

URL = 'https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/plan.php?y=24-25&t=s1&AC.T.2=AC.T.2&AC.S.1=AC.S.1&AC.L.5=AC.L.5&AC.TG.5=AC.TG.5&RI.T.2=RI.T.2&RI.S.1=RI.S.1&RI.L.7=RI.L.7&RI.TG.7=RI.TG.7&CVVS.T.1=CVVS.T.1&CVVS.S.3=CVVS.S.3&CVVS.L.9=CVVS.L.9&CVVS.TG.9=CVVS.TG.9&SI.T.1=SI.T.1&SI.S.-=SI.S.-&SI.L.9=SI.L.9&SI.TG.9=SI.TG.9&SR.T.1=SR.T.1&SR.S.1=SR.S.1&SR.L.2=SR.L.2&SR.TG.2=SR.TG.2&vista=tabla'
asignaturas = ["RI","AC","CVVS","SI","SR"]
tiposClases         = ["T","TG","S","L"]
nMaxDiferentesTipos = [4  ,20  ,6  ,20]

cabecera = """<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1252"><title>Planificación de asignaturas</title></head>
<body>
<h1>Planificación de asignaturas</h1>
<table border="1"><tbody><tr><td>&nbsp; </td><td bgcolor="White">Lunes, 30/01/2023</td><td bgcolor="White">Martes, 31/01/2023</td><td bgcolor="White">Miércoles, 01/02/2023</td><td bgcolor="White">Jueves, 02/02/2023</td><td bgcolor="White">Viernes, 03/02/2023</td><td bgcolor="Salmon">Sábado, 04/02/2023</td><td bgcolor="Salmon">Domingo, 05/02/2023</td></tr>
"""

import time



h1file = Constantes.DATA_DIRECTORY+"h1.html"
h2file = Constantes.DATA_DIRECTORY+"h2.html"


def generateHtml():

    inicio = time.time()

    f1 = open(h1file, 'r', encoding='latin-1')
    f2 = open(h2file, 'r', encoding='latin-1')

    dataF1 = f1.readlines()
    dataF2 = f2.readlines()


    print(len(dataF1), " - ", len(dataF2))






    f1.close()
    f2.close()


    final = time.time()
    print(final-inicio)


# ------------------------------------------------------------------------------


def getMenuOptions():
    return ["1_ Generar html",
            "0_ Salir"]


def main():

    Utils.say("Starting...")

    while(True):
        InterfazUtils.showMenu("Menú", getMenuOptions())

        option = Utils.askInt("Opcion?")
        if(option == 0):
            exit(0)

        elif(option == 1):
            generateHtml(URL)

        else:
            msg =">> Opción ["+str(option) +"] no existe"
            Utils.say(msg)
            continue


generateHtml()

