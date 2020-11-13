import os
from tkinter import *
from tkinter import ttk
from OperacionesCliente import inicio_comparacion_firmas
from Cliente import obtenerFirmas, MainC
import threading
from datetime import datetime, time, timedelta
import time
from tkinter import filedialog

#Variables globales
firmas = ""
escaneo = ""
tInfoEscaneo = ""

#funcion que hace llamado a la funcion para un escaneo inmediato
def ejecutarEscaneo(carpeta):

    global firmas
    inicio_comparacion_firmas(carpeta, firmas)


#Función para los escaneos programados, en la que se valida la cantidad de dias seleccionada como frecuencia y la hora deseada
def escanear():
    while True:
        now = datetime.now()
        fecha = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        global escaneo
        print("g= "+escaneo[1]+" n= "+fecha)
        if fecha == escaneo[1]:
            print("g= "+escaneo[2]+" n= "+str(now.hour))
            if str(now.hour) >= escaneo[2]:
                # actaulizar programado
                if escaneo[0] == "Diario":
                    nuevaFecha = now + timedelta(days=1)
                    fecha = str(nuevaFecha.year) + "-" + str(nuevaFecha.month) + "-" + str(nuevaFecha.day)
                    escaneo[1] = fecha
                else:
                    if escaneo[0] == "Semanal":
                        nuevaFecha = now + timedelta(days=8)
                        fecha = str(nuevaFecha.year) + "-" + str(nuevaFecha.month) + "-" + str(nuevaFecha.day)
                        escaneo[1] = fecha
                    else:
                        nuevaFecha = now + timedelta(days=30)
                        fecha = str(nuevaFecha.year) + "-" + str(nuevaFecha.month) + "-" + str(nuevaFecha.day)
                        escaneo[1] = fecha

                # realizar escaneo
                global firmas
                inicio_comparacion_firmas(escaneo[3], firmas)

        time.sleep(60)



#Clase de la ventana para el cliente
class VentanaCliente():

    def __init__(self):
            # Da tamaño a la ventana
            self.raiz = Tk()
            self.raiz.geometry('500x500')

            # Impide que cambiar el tamaño a la ventana
            self.raiz.resizable(width=False, height=False)
            self.raiz.title('Cliente')

            # etiquetas
            lbTiempo = Label(self.raiz, text="Tiempo").place(x=10, y=10)
            lbHora = Label(self.raiz, text="Hora").place(x=10, y=40)
            lbTipo = Label(self.raiz, text="Tipo").place(x=10, y=70)
            lbCarpeta = Label(self.raiz, text="Ruta de carpeta para escaneo programado").place(x=10, y=100)
            lbDatosEscaneo = Label(self.raiz, text="Datos Escaneo").place(x=10, y=180)
            lbAhora = Label(self.raiz, text="Escanear Ahora").place(x=10, y=270)
            lbCarpetaAhora = Label(self.raiz, text="Ruta de carpeta a escanear").place(x=10, y=310)

            #ingresar Informacion
            self.listaDesplegable = ttk.Combobox(self.raiz, width=17, state='readonly')
            self.listaDesplegable.place(x=100, y=10)
            opciones = ["Diario", "Semanal", "Mensual"]
            self.listaDesplegable['values'] = opciones
            self.listaDesplegable.set(opciones[0])

            self.listaDesplegableHora = ttk.Combobox(self.raiz, width=17, state='readonly')
            self.listaDesplegableHora.place(x=100, y=40)
            opciones = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
                        "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
                        "21", "22", "23", "24"]
            self.listaDesplegableHora['values'] = opciones
            self.listaDesplegableHora.set(opciones[0])

            # mostrar Informacion
            self.tinfo = Text(self.raiz, width=59, height=2)
            self.tinfo.place(x=10, y=130)

            self.tinfoAhora = Text(self.raiz, width=59, height=2)
            self.tinfoAhora.place(x=10, y=330)

            self.tinfoEscaneo = Text(self.raiz, width=59, height=2)
            self.tinfoEscaneo.place(x=10, y=210)

            # Crea Button programarEscaneo, asigna accion y posicion
            self.bEscaneo = ttk.Button(self.raiz, text='Escoger Carpeta', command=self.programarEscaneo)
            self.bEscaneo.place(x=100, y=70)

            self.bCompleto = ttk.Button(self.raiz, text='Completo', command=self.escaneoCompleto)
            self.bCompleto.place(x=200, y=70)

            self.bEscaneoAhora = ttk.Button(self.raiz, text='Escoger Carpeta', command=self.programarEscaneoAhora)
            self.bEscaneoAhora.place(x=100, y=270)

            self.bCompletoAhora = ttk.Button(self.raiz, text='Completo', command=self.escaneoCompletoAhora)
            self.bCompletoAhora.place(x=200, y=270)

            # Pone foco en el boton ver info entonces se selecciona si se le da a la barra espaciadora
            self.bEscaneo.focus_set()
            self.raiz.mainloop()

            # Funcion que finaliza la ejecución del servidor

    def on_closing(self):
        sys.exit()

    #Función para escanear de manera completa el sistema de acuerdo a la frecuencia y hora programada
    def escaneoCompleto(self):
        self.tinfo.delete("1.0", END)
        tiempo = self.listaDesplegable.get()
        hora = self.listaDesplegableHora.get()
        carpeta = str(os.path.abspath('Proyecto1Redes').split(os.path.sep)[0]+os.path.sep)
        self.tinfo.insert("1.0", carpeta)
        texto = "Tiempo: "+str(tiempo)+" Hora: "+str(hora)+"\nRuta Carpeta: "+str(carpeta)
        self.tinfoEscaneo.insert("1.0", texto)

        global escaneo
        now = datetime.now()
        fecha = str(now.year) + "-" + str(now.month) + "-" + str(now.day)
        escaneo = [str(tiempo), fecha, str(hora), carpeta]

        t1 = threading.Thread(target=escanear)
        t1.daemon = True
        t1.start()

    #Se encarga de programar el escaneo de una carpeda
    def programarEscaneo(self):
        self.tinfo.delete("1.0", END)
        directorio = filedialog.askdirectory()
        tiempo = self.listaDesplegable.get()
        hora = self.listaDesplegableHora.get()
        self.tinfo.insert("1.0", str(directorio))
        texto = "Tiempo: "+str(tiempo)+" Hora: "+str(hora)+"\nRuta Carpeta: "+str(directorio)
        self.tinfoEscaneo.insert("1.0", texto)

        global escaneo
        now = datetime.now()
        fecha = str(now.year)+"-"+str(now.month)+"-"+str(now.day)
        escaneo = [str(tiempo), fecha, str(hora), str(directorio)]

        t1 = threading.Thread(target=escanear)
        t1.daemon = True
        t1.start()

    #Escanea de manera inmediata el sistema completo
    def escaneoCompletoAhora(self):
        carpeta = str(os.path.abspath('Proyecto1Redes').split(os.path.sep)[0] + os.path.sep)
        self.tinfoAhora.delete("1.0", END)
        self.tinfoAhora.insert("1.0", carpeta)

        t1 = threading.Thread(target=ejecutarEscaneo, args=(carpeta,))
        t1.daemon = True
        t1.start()

    #Escanea la carpeda seleccionada por el usuario de manera inmediata
    def programarEscaneoAhora(self):
        self.tinfoAhora.delete("1.0", END)
        directorio = filedialog.askdirectory()
        self.tinfoAhora.insert("1.0", str(directorio))

        t1 = threading.Thread(target=ejecutarEscaneo, args=(directorio,))
        t1.daemon = True
        t1.start()

#Función main
def Main():
    MainC()

    global firmas
    firmas = obtenerFirmas()
    app = VentanaCliente()
    return 0

#Main()

# global firmas
# inicio_comparacion_firmas(os.path.abspath('Proyecto1Redes').split(os.path.sep)[0]+os.path.sep, firmas)
# inicio_comparacion_firmas("C:/Users/Steven/Desktop/PruebaProyectoRedes2", firmas)s