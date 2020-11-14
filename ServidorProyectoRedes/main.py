import threading
import Ventana
from Servidor import MainS


#función de inicio de la ventana para el servidor
def iniciaVentana():
    Ventana.main()

#función de inicio para el servidor
def iniciaServidor():
    MainS()

if __name__ == '__main__':
    #Se inician los hilos que levantan el servidor y la ventana del mismo
    t1 = threading.Thread(target=iniciaVentana)
    t2 = threading.Thread(target=iniciaServidor)
    t2.daemon = True
    t1.start()
    t2.start()