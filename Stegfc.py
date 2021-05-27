#Prueba esteganografia

import os
import os.path
from zipfile import ZipFile

#Esta parte comprime todos los archivos .txt
lista = os.listdir()
myzip = ZipFile('secreto.zip','w')
for archivo in lista:
    nombre, extension = os.path.splitext(archivo)
    if extension == '.txt':
        myzip.write(archivo)
    if extension == '.jpg':
        imagen = archivo
myzip.close()
        
#Esta parte une los archivos
ocultar = open('secreto.zip','rb')
cortina= open(imagen,'ab')
mensaje = ocultar.read()
cortina.write(mensaje)
ocultar.close()
cortina.close()

#Borra archivos ocultados
for archivo in lista:
    nombre, extension = os.path.splitext(archivo)
    if extension == '.txt':
        os.remove(archivo)
os.remove('secreto.zip')
