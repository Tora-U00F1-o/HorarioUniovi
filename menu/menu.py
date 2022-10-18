def cero():
    print("opcion 0")

def uno():
    print("opcion 1")

def dos():
    print("opcion 2")

def tres():
    print("opcion 3")

class Menu():
    title = ""
    content = []

    def __init__(self, title):
        self.title = title

    def toStringFormated(self):
        return self._hInicio+" - "+self._hFinal+"\t"+self._nombre

    def addItem(self, item):
        self.content.append(item)

    def execute(self, index):
        self.content[index][1]()


    def showMenu(self):
        print("\n-----------------------------\n"
            +" "+self.title+"\n"
            +"-----------------------------")

        index = 0
        for option in self.content:
            print(index,"_ ",option[0])
            index+=1

        print("-----------------------------")







"""
menu item --- texto
function item -- func

submenu -- menu nuevo


"""





def getMenuOptions():
    return [
        ["Salir", cero],
        ["Horario de Hoy", uno],
        ["Otra Fecha", dos],
        ["Mostrar Fecha de Hoy", tres],
    ]

def main():

    options = getMenuOptions()
    menu = Menu("Prueba")

    for option in options:
        menu.addItem(option)

    menu.showMenu()


##    while(True):
##        options = getMenuOptions()
##        showMenu("Menú", options)
##
##
##        option = askInt("Opcion?")
##
##        print("opcion elegida ->"+options.keys()[option]+"<-")
##        options[options.keys[option]]()
##
##
##        if(0<option>=len(getMenuOptions().items())):
##            msg =">> Opción ["+str(option) +"] no existe"
##            print(msg)
##            continue


main()

