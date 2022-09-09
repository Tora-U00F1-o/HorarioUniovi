
#para parse
NOMBRE_POS = 0
FECHA_POS = 1
H_INICIO_POS = 2
H_FINAL_POS = 4

# Subject ------------------------------------------------------------------------
class Subject():
    _nombre = ""
    _fecha = ""
    _hInicio = ""
    _hFinal = ""

    def initSubject(self, nombre, fecha, hInicio, hFinal):
        self._nombre = nombre
        self._fecha = fecha
        self._hInicio = hInicio
        self._hFinal = hFinal

    def toStringFormated(self):
        return self._hInicio+" - "+self._hFinal+"\t"+self._nombre

def newSubject(nombre, fecha, hInicio, hFinal):
    c = Subject()
    c.initSubject(nombre, fecha, hInicio, hFinal)
    return c

"""Devuelve un array de texto de las asignaturas dadas"""
def formatArraySubjects(array = []):
    result = []
    for clase in array:
        result.append(clase.toStringFormated())
    return result

"""Devuelve un array de asignaturas ordenado apartir de otro array dado"""
def sortArraySubjects(array = []):
    sortedSubjects = []
    sortedSubjects.append(array[0])
    for i in range(1, len(array)):
        for j in range(len(sortedSubjects)):
            if(array[i]._hInicio<sortedSubjects[j]._hInicio):
                sortedSubjects.insert(j, array[i])
                break

            if(j+1==len(sortedSubjects)):
                sortedSubjects.append(array[i])
                break

    return sortedSubjects

"""Apartir de un array de asignaturas """
def procesSubjectsParsed(array = []):
    sortedSubjects = sortArraySubjects(array)
    return formatArraySubjects(sortedSubjects)


# Parse Subject ------------------------------------------------------------------

    # EJ: "AC.T.1, 16/11/2020,  18.00,16/11/2020, 20.00,Hora de clase n\xfamero 14 de AC.T.1, Online"
def parseArraySubject(array = []):
    result = []
    for clase in array:
        result.append(parseSubject(clase))
    return result

def parseSubject(claseString):
    data = claseString.split(r",")
    nombre = data[NOMBRE_POS].strip()
    fecha = data[FECHA_POS].strip()
    hInicio = data[H_INICIO_POS].strip()
    hFinal = data[H_FINAL_POS].strip()
    return newSubject(nombre, fecha, hInicio, hFinal)
