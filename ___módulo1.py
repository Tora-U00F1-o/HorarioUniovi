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

def resetDatos(url):
    p = url.split('&')
    f=open(arch,'w')
    for p2 in p:
        f.write(p2+"\n")
    f.close()


def cargar():
    urlNueva = ""
    f=open(arch,'r')
    array = f.readlines()
    for i in range(len(array)):
        urlNueva += array[i].strip()
        if(i<len(array)-1):
            urlNueva += '&'
    f.close()
    return urlNueva

def buscarNombreAsignaturasEnWeb(url):
    urlCSV = Utils.processVistaURL(url, WebUtils.CSV)
    req = requests.get(urlCSV, verify=False)
    data = req.text
    s = []
    for l in str(data).split("\n"):
        asig =l.split(",")[0]
        if asig not in s:
            s.append(asig)
    s = s[1:]
    return s

def getCodigoAsigFormateada(nAsig, tipo, num, ch):
    return asignaturas[nAsig] +ch +tipo +ch +str(num)

def generarConvinacionesPosiblesGruposAsignatura(nAsig):
    array = []
    for i in range(len(tiposClases)):
        tipo = tiposClases[i]
        for num in range(1, nMaxDiferentesTipos[i]+1):
            pri = getCodigoAsigFormateada(nAsig, tipo, num, "_")
            seg = getCodigoAsigFormateada(nAsig, tipo, num, ".")
            array.append(pri+"="+seg)
    return array

def generarURL(arrayPosiblesAsignaturas):
    urlNueva = "https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/plan.php?vista=csv&y=24-25&t=s1&"

    for i in range(len(arrayPosiblesAsignaturas)):
        urlNueva += arrayPosiblesAsignaturas[i]
        if(i<len(arrayPosiblesAsignaturas)-1):
            urlNueva += '&'

    return urlNueva


def buscarGruposAsignaturas(nAsig, junto=0):
    # hacemos la url
    conv = []
    if(junto):
        for i in range(len(asignaturas)):
            conv += generarConvinacionesPosiblesGruposAsignatura(i)

    else:
        conv = generarConvinacionesPosiblesGruposAsignatura(nAsig)

    urlNueva = generarURL(conv)

    #lo contrastamos con la web
    nombres = buscarNombreAsignaturasEnWeb(urlNueva)
    return urlNueva

def mostrarAsigJuntas():
    #cada asignatura por separado
    for i in range(len(asignaturas)):
        url = buscarGruposAsignaturas(i)
        WebUtils.open(url, WebUtils.TABLA)

    #todas en el mismo calendario
    url = buscarGruposAsignaturas(0,1)
    WebUtils.open(url, WebUtils.TABLA)
    return url



# ------------------------------------------------------------------------------


def getMenuOptions():
    return ["1_ Horarios de asignatura",
            "2_ Cargar desde archivo",
            "3_ Mostrar tabla en navegador",
            "4_ Mostrar web en navegador",
            "5_ Reset archivo",
            "6_ Convinaciones de asignaturas",
            "7_ Abrir carpeta en Explorer",
            "0_ Salir"]


def main():

    urla = ""

    Utils.say("Starting...")
    if(urla==""):
##        resetDatos(URL)
        urla = cargar()
    Utils.say("Ready")


    while(True):
        InterfazUtils.showMenu("Menú", getMenuOptions())

        option = Utils.askInt("Opcion?")
        if(option == 0):
            exit(0)

        elif(option == 1):
            nAsig = Utils.askInt("numero asignatura [0:] \n"+str(asignaturas)+"\n [  0,     1,     2,     3,     4]")
            urlTemp = buscarGruposAsignaturas(nAsig)
            option = Utils.askInt("cargar? [*respuesta es num]")
            if(option):
                urla = urlTemp
                resetDatos(urla)

        elif(option == 2):
            urla = cargar()

        elif(option == 3):
             WebUtils.open(urla, WebUtils.TABLA)

        elif(option == 4):
            WebUtils.open(urla, WebUtils.WEB)

        elif(option == 5):
            resetDatos(URL)

        elif(option == 6):
            urlTemp = mostrarAsigJuntas()
            resetDatos(urlTemp)

        elif(option == 7):
            ExplorerUtils.openInExplorer(Constantes.FILE_NAME)

        elif(option == 8):
            ExplorerUtils.getFilesFromDirectory(arch)

        else:
            msg =">> Opción ["+str(option) +"] no existe"
            Utils.say(msg)
            continue


main()

