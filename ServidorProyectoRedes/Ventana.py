from builtins import SystemExit
import sys
from tkinter import *
from tkinter import ttk
from Configuracion import mysql_connection, get_data_from_sql

#Clase de la ventana que se muestra en el servidor
class Ventana():
    def __init__(self):
            # Da tamaño a la ventana
            self.raiz = Tk()
            self.raiz.geometry('600x500')
            self.raiz.protocol("WM_DELETE_WINDOW", self.on_closing)

            # Impide que cambiar el tamaño a la ventana
            self.raiz.resizable(width=False, height=False)
            self.raiz.title('Servidor')

            # Crea widget Text y asigna posicion
            self.tinfo = Text(self.raiz, width=110, height=25)
            self.tinfo.pack(side=TOP)

            # Crea Button verClientes, asigna accion y posicion
            self.binfo = ttk.Button(self.raiz, text='Ver Clientes', command=self.verClientes)
            self.binfo.pack(side=LEFT)

            # Crea Button verArchivosPeligrosos, asigna accion y posicion
            self.bArchi = ttk.Button(self.raiz, text='Ver Archivos', command=self.verArchivosPeligrosos)
            self.bArchi.pack(side=LEFT)

            # Pone foco en el boton ver info entonces se selecciona si se le da a la barra espaciadora
            self.binfo.focus_set()
            self.raiz.mainloop()

    #Funcion que finaliza la ejecución del servidor
    def on_closing(self):
        sys.exit()

    #Función que muestra los clientes que están registrados en la base de datos
    def verClientes(self):
        # Borra el contenido de la caja de texto
        self.tinfo.delete("1.0", END)
        texto = "ID  |  Direccion ip\n"

        # Obtiene información de la ventana 'self.raiz':
        sp = 'Select id, direccionIp from clientes'
        con_mysql = mysql_connection()
        data = get_data_from_sql(sp)

        if len(data) <= 0:
            print('No Data')
            sys.exit(0)
        else:
            # Construye una cadena de texto con toda la
            # información obtenida:
            for row in data:
                texto += str(row[0])+"     "+row[1]+"\n"

        # Inserta la información en la caja de texto:
        self.tinfo.insert("1.0", texto)

    #Función que muestra los archivos peligrosos y el usuario que los detectó, junto con la cantidad de detecciones por cada cliente
    def verArchivosPeligrosos(self):
        # Borra el contenido de la caja de texto
        self.tinfo.delete("1.0", END)
        texto = "   IP          |     Total    |    Archivo     \n"

        # Obtiene información de la ventana 'self.raiz':
        sp = 'select c.direccionIp, a.nombre , count(*) as cantidadDetecciones from cliente_archivo ca join archivospeligrosos a on a.id = ca.idArchivoPeligroso join clientes c on c.id = ca.idCliente GROUP BY ca.idArchivoPeligroso, ca.idCliente ORDER BY c.direccionIp asc;'
        con_mysql = mysql_connection()
        data = get_data_from_sql(sp)

        if len(data) <= 0:
            print('No Data')
            sys.exit(0)
        else:
            # Construye una cadena de texto con toda la
            # información obtenida:
            for row in data:
                texto += row[0] + "         " + str(row[2]) + "          " + row[1] + "\n"

        # Inserta la información en la caja de texto:
        self.tinfo.insert("1.0", texto)

#Función main
def main():
    app = Ventana()
    return 0
