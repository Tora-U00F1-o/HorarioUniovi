
import csv
from io import StringIO
import requests

# URL de la página web que contiene la tabla
url = 'https://gobierno.ingenieriainformatica.uniovi.es/grado/gd/?y=24-25&t=s1'

# Realizar una solicitud GET para obtener el contenido HTML de la página
response = requests.get(url, verify=False)

# Verificar si la solicitud fue exitosa (código de respuesta 200)
if response.status_code == 200:
    # Obtener el contenido HTML como una cadena
    html_content = response.text

    # Buscar la tabla en el contenido HTML
    # Supongamos que la tabla está entre etiquetas <table> y </table>
    start = html_content.find("<table")
    end = html_content.find("</table", start)

    # Extraer la porción de HTML que contiene la tabla
    table_html = html_content[start:end+8]  # Añadir 8 caracteres para incluir la etiqueta de cierre </table>

    # Leer la tabla utilizando csv.reader y StringIO
    table_io = StringIO(table_html)
    reader = csv.reader(table_io)




    # Convertir los datos de la tabla en una lista de listas (array)
    table_array = [row for row in reader]

    # Imprimir el array
    ia = 0
    for row in table_array:
        ia+=1
        if(ia < 1):
            print("\n")
            print("\n")
            print(row)

    array = []
    for i in range (0, 1):#len(table_array)):
        print(table_array[i])


else:
    print(f"No se pudo acceder a la página web. Código de respuesta: {response.status_code}")


