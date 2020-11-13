import threading
import VentanaCliente


#función de inicio de la ventana para el servidor
def iniciarCliente():
    VentanaCliente.Main()

if __name__ == '__main__':
    t1 = threading.Thread(target=iniciarCliente)
    t1.start()

