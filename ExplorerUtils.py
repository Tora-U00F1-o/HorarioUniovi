import os
import subprocess

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'),'explorer.exe')
def openInExplorer(path):# explorer would choke on forward slashes
    path = os.path.normpath(path)
    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH,'/select,', os.path.normpath(path)])



def getFilesFromDirectory(path):
    print(os.listdir(path)) #con esto se ve las cosas de una carpeta
