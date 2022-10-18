
def cero():
    print("opcion 0")

def uno():
    print("opcion 1")

def dos():
    print("opcion 2")

def tres():
    print("opcion 3")

"""
a_dict = {"A": uno, "B": dos, "C": tres}

x = a_dict.items()


a_dict["A"]()

print(a_dict.get(1))
a_dict.

a_dict.get(1)()


print("fin")

"""

def ask(mensaje):
    return input(str(mensaje))


def askInt(mensaje):
    while(True):
        try:
            return int(ask(mensaje))
        except ValueError:
            continue



##def getMenuOptions():
##    return {
##    "0_ Salir": cero,
##    "1_ Horario de Hoy": uno,
##    "2_ Otra Fecha": dos,
##    "3_ Mostrar Fecha de Hoy": tres,
##    }

def getMenuOptions():
    return [
        ["Salir", cero],
        ["Horario de Hoy", uno],
        ["Otra Fecha", dos],
        ["Mostrar Fecha de Hoy", tres],
    ]


def showMenu(title, options = []):
    print("\n-----------------------------\n"
        +"-----------------------------\n"
        +" "+title+"\n")

    index = 0
    for option in options:
        print(index,"_ ",option[0])
        index+=1

    print("-----------------------------")

def execute(index):
    options = getMenuOptions()


def main():

    options = getMenuOptions()
    print(options[3])
    options[3][1]()

    while(True):
        options = getMenuOptions()
        showMenu("Menú", options)


        option = askInt("Opcion?")

        if(0<option>=len(options)):
            msg =">> Opción ["+str(option) +"] no existe"
            print(msg)
            continue

        print("opcion elegida ->", options[option],"<-")
        options[option][1]()

main()

