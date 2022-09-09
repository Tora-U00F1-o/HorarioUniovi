import Constantes
import Utils

import webbrowser

## Esto es pq hay un warning de que no se comprueba el http
## (a dia de 18/04/2022 no funciona la web
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# tipos de vista URL (parametro de URL "vista")
# [web , csv , ]
WEB = 'web'
CSV = 'csv'
TABLA = 'tabla'

def open(type):
    open(Constantes.URL, type)

def open(url, type):
    urlNew = Utils.processVistaURL(url, type)
    webbrowser.open(urlNew)

