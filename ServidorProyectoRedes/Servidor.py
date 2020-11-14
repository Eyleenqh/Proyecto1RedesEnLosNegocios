import socket
from Configuracion import get_data_from_sql, set_data_from_sql
from _thread import *


# thread function
def threaded(c,addr):
    while True:
        data = c.recv(1024)
        if not data:
            print('Bye')
            break


        # reverse the given string from client
        if (str(data.decode('ascii')) == "conectando"):
           mensaje = "conectado"
           c.send(mensaje.encode('ascii'))
           data = c.recv(1024)
           ip = str(data.decode('ascii'))
           insertar_cliente(ip)
           enviarHash(c)
           break

        if (str(data.decode('ascii')) == "detectados"):
            mensaje = "listo"
            c.send(mensaje.encode('ascii'))
            # recibo ip
            data = c.recv(1024)
            ip = str(data.decode('ascii'))
            print(ip)
            mensaje = "esperando"
            c.send(mensaje.encode('ascii'))
            # recibo archivos detectados
            data = c.recv(1024)
            insertar_Detectados(str(data.decode('ascii')), ip)

        # connection closed
        break
    print("Cerro conexion")
    c.close()

#Función que obtiene las firmas de los archivos peligrosos de la base de datos
def obtener_archivos():
    #obtener los datos
    texto = ""
    sp = 'SELECT firma from archivosPeligrosos'
    data = get_data_from_sql(sp)

    if len(data) <= 0:
        print('No Data')
    else:
        # Construye una cadena de texto con toda la
        # información obtenida:
        for row in data:
            texto += str(row[0])+ ","
    largo = len(texto)
    textofinal = texto[:largo - 1]
    return textofinal

#Función que envía las firmas al cliente
def enviarHash(c):
    data = obtener_archivos()
    c.send(data.encode('ascii'))

#Función que inserta en la base de datos la información de un cliente que se conecta por primera vez
def insertar_cliente(direccion):
    id = obtener_cliente(direccion)
    if id == '':
        sp = ("INSERT INTO clientes "
              "(direccionIp) "
            "VALUES ('"+direccion+"')")
        set_data_from_sql(sp)

#Función que busca el id del cliente en la base de datos con la dirección ip que le llega como parámetro
def obtener_cliente(ip):
    print("esta ip viene ", ip)
    texto = ''
    sp = "SELECT id from clientes where direccionIp='"+ip+"'"
    data = get_data_from_sql(sp)

    if len(data) <= 0:
        print('No Data')
    else:
        for row in data:
            texto = str(row[0])
    return texto

#Función que obtiene el id del archivo peligroso de la base de datos con la firma que le llega como parámetro
def obtener_archivo(archivo):
    texto = ''
    sp = "SELECT id from archivosPeligrosos where firma='"+archivo+"'"
    data = get_data_from_sql(sp)

    if len(data) <= 0:
        print('No Data')
    else:
        for row in data:
            texto = str(row[0])
    return texto

#Función que inserta las detecciones del cliente en la base de datos
def insertar_Detectados(detectados, ip):
    idCliente = obtener_cliente(ip)
    lista_detectados = detectados.split(sep=',')

    for archivo in lista_detectados:
        idArchivo = obtener_archivo(archivo)
        sp = ("INSERT INTO cliente_archivo"
        "(idCliente,idArchivoPeligroso)"
        "VALUES("+idCliente+","+idArchivo+")")
        set_data_from_sql(sp)

#Función main
def MainS():
    host = ""

    # reverse a port on your computer
    # in our case it is 12345 but it
    # can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)


    # a forever loop until client wants to exit
    while True:
        # put the socket into listening mode
        s.listen(5)
        print("socket is listening")
        # establish connection with client
        c, addr = s.accept()

        print('Connected to :', addr[0], ':', addr[1])

        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,addr))
    s.close()

#MainS()