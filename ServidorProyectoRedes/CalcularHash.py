#from tkinter.filedialog import askopenfilename
import hashlib
import os, sys

#Función de MD5 para calcular el hash de los archivos peligrosos iniciales que se tendrán como muestra
def hashing():
    path = "ruta deseada"
    lista_de_archivos = os.listdir(path)
    i = 1

    #Se recorren todos los archivos encontrados en el directorio y se le calcula el hash para generar los inserts a la base de datos que
    #funcionarán como las firmas de archivos peligrosos
    for archivo in lista_de_archivos:
        rutaArchivo = "ruta deseada"+archivo
        curfile = open(rutaArchivo, "rb")
        hasher = hashlib.md5()
        buf = curfile.read()
        hasher.update(buf)
        print("insert into archivosPeligrosos(nombre, firma) values ('"+archivo+"','"+hasher.hexdigest()+"')")
        curfile.close()


hashing()
