import WebUtils
import Utils


import csv
from io import StringIO
import requests



arch = "___p.txt"

URL = "https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/plan.php?vista=tabla&y=22-23&t=s1&AL_T_2=AL.T.2&AL_S_3=AL.S.3&AL_L_8=AL.L.8&Cal_T_2=Cal.T.2&Cal_S_3=Cal.S.3&Cal_L_8=Cal.L.8&DS_T_3=DS.T.3&DS_S_3=DS.S.3&DS_L_5=DS.L.5&DS_TG_5=DS.TG.5&IPS_T_1=IPS.T.1&IPS_S_3=IPS.S.3&IPS_L_6=IPS.L.6&IPS_TG_6=IPS.TG.6&RI_T_2=RI.T.2&RI_S_3=RI.S.3&RI_L_8=RI.L.8&RI_TG_8=RI.TG.8"
asignaturas = ["AL","Cal","DS","IPS","RI"]
tiposClases         = ["T","TG","S","L"]
nMaxDiferentesTipos = [4  ,20  ,4  ,20]

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
        urlNueva += array[i][:-1]
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
    urlNueva = "https://gobierno.ingenieriainformatica.uniovi.es/grado/plan/plan.php?vista=tabla&y=22-23&t=s1&"

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
    return ["1_ Magia pa",
            "2_ Cargar desde archivo",
            "3_ Mostrar tabla en navegador",
            "4_ Mostrar web en navegador",
            "5_ Reset archivo",
            "6_ Convinaciones de asignaturas",
            "0_ Salir"]

"""Imprime el menu introducido, se añade una cabecera"""
def showMenu(title, options = []):
    Utils.say("\n-----------------------------\n"
        +"-----------------------------\n"
        +" "+title+"\n"
        +"-----------------------------")

    for option in options:
        Utils.say("  "+option)

    Utils.say("-----------------------------")

def main():

    urla = ""

    Utils.say("Starting...")
    if(urla==""):
##        resetDatos(URL)
        urla = cargar()
    Utils.say("Ready")


    while(True):
        showMenu("Menú", getMenuOptions())

        option = Utils.askInt("Opcion?")
        if(option == 0):
            exit(0)

        elif(option == 1):
            nAsig = Utils.askInt("numero asignatura [0:] "+str(asignaturas))
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

        else:
            msg =">> Opción ["+str(option) +"] no existe"
            Utils.say(msg)
            continue


main()

