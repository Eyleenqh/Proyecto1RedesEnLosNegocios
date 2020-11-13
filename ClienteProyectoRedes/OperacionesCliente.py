import os
import hashlib
import threading
from Cliente import enviarDetectados
from tkinter import *

detecciones = ""
rutas = ""

#Función que envia las detecciones que se tienen en el cliente hacia el servidor
def enviar_detecciones_cliente(detectados):
    if detectados != "":
        enviarDetectados(detectados)
        global detecciones
        detecciones = ""
        global rutas
        VentanaDetectados(rutas)
        rutas = ""
    else:
        VentanaDetectados("No se encontraron Archivos Peligrosos")

##Clase de la ventana que muestra el resultado del análisis
class VentanaDetectados():

    def __init__(self, detectados):
        self.raiz2 = Tk()
        self.raiz2.geometry('500x200')
        self.raiz2.resizable(width=False, height=False)
        self.raiz2.title('Reporte Detectados')

        lbFirmasDetectadas = Label(self.raiz2, text="Archivos peligrosos: ").place(x=10, y=10)
        self.tinfoDetectados = Text(self.raiz2, width=59, height=9)
        self.tinfoDetectados.place(x=10, y=40)

        self.tinfoDetectados.delete("1.0", END)
        largo = len(detectados)
        texto = detectados[:largo - 1]
        data = texto.split(sep=',')
        textoFinal = ""
        for row in data:
            textoFinal += "* "+row + "\n"

        self.tinfoDetectados.insert("1.0", textoFinal)
        self.raiz2.mainloop()


#Función que inicia el hilo que comparan las firmas que vienen del servidor con el hash de los archivos analizados y
#el hilo que envia las detecciones al servidor
def inicio_comparacion_firmas(path, firmas):
    t1 = threading.Thread(target=comparar_firmas, args=(path, firmas))
    t1.daemon = True
    t1.start()
    t1.join()

    global detecciones
    t2 = threading.Thread(target=enviar_detecciones_cliente, args=(detecciones,))
    t2.daemon = True
    t2.start()

#Función que compara las firmas que vienen del servidor con el hash de los archivos que se encuentran en la ruta proporcionada y
# sus respectivos subdirectorios (Función recursiva)
def comparar_firmas(path, firmas):

    #Revisa todos los archivos que se encuentran en la ruta que viene como parámetro
    for entry in os.scandir(path):
        print(entry.path)
        try:
            is_dir = entry.is_dir(follow_symlinks=False)
        except OSError as error:
            print('Error calling is_dir():', error, file=sys.stderr)
            continue
        if is_dir:
            try:
                comparar_firmas(entry.path, firmas)
            except PermissionError:
                print("Sin acceso a", entry.path)
                continue
        else:
            #calcula el hash del archivo
            try:
                curfile = open(entry.path, "rb")
                hasher = hashlib.md5()
                buf = curfile.read()
                hasher.update(buf)
                curfile.close()

                #compara las firmas con el hash del archivo
                for firma in firmas:
                    if firma == str(hasher.hexdigest()):
                        print(firma + " -vs- " + str(hasher.hexdigest()))
                        global detecciones
                        detecciones += str(hasher.hexdigest()) + ','
                        global rutas
                        rutas += str(entry.path) + ','
                    else:
                        continue
            except OSError as error:
                print('Error calling stat():', error, file=sys.stderr)

    return detecciones
