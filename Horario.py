import Subject
import Persistencia
import Utils
import Constantes
import WebUtils
import InterfazUtils


#Interfaz ----------------------------------------------------------------------

def showHorario(fecha, horario = []):
    InterfazUtils.showMenu("Horario "+fecha, horario)

def getMenuOptions():
    return ["1_ Horario de Hoy",
            "2_ Otra Fecha",
            "3_ Mostrar Fecha de Hoy",
            "4_ Actualizar Base Datos",
            "5_ Mostrar tabla en navegador",
            "6_ Mostrar web en navegador",
            "0_ Salir"]


# Main -------------------------------------------------------------------------
def program(fecha):
    try:
        subjectsString = Persistencia.getSubjectByDate(fecha)

    except ValueError:
        Utils.say(">> No hay nada en esa fecha - ("+fecha+")")
        return

    subjectsParsed = Subject.parseArraySubject(subjectsString)
    subjectsFormated = Subject.procesSubjectsParsed(subjectsParsed)

    showHorario(fecha, subjectsFormated)


def main():
    fecha = Utils.getTodayDate()
    if(Persistencia.hasToUpdateDB()):
        Persistencia.updateDB()

    while(True):
        InterfazUtils.showMenu("Menú", getMenuOptions())

        option = Utils.askInt("Opcion?")
        if(option == 0):
            exit(0)

        elif(option == 1):
            program(Constantes.todayDate)
            continue

        elif(option == 2):
            otherDate = Utils.ask("Que fecha quieres ver? (dd/mm/YYYY)")
            if(otherDate.strip() == ""):
                continue
            otherDate = Utils.processDate(otherDate);
            program(otherDate)
            continue

        elif(option == 3):
            Utils.say("La fecha de hoy es "+ Constantes.todayDate)
            continue

        elif(option == 4):
            Persistencia.updateDB()
            continue

        elif(option == 5):
            WebUtils.open(WebUtils.TABLA)

        elif(option == 6):
            WebUtils.open(WebUtils.WEB)

        else:
            msg =">> Opción ["+str(option) +"] no existe"
            Utils.say(msg)
            continue


main()
