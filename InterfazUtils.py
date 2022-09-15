import Utils

"""Imprime el menu introducido, se añade una cabecera"""
def showMenu(title, options = []):
    Utils.say("\n-----------------------------\n"
        +"-----------------------------\n"
        +" "+title+"\n"
        +"-----------------------------")

    for option in options:
        Utils.say("  "+option)

    Utils.say("-----------------------------")
