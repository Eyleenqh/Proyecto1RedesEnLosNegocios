# Import socket module
import socket

#Variables globales
firmas = ""

#Función que retorna las firmas que vienen del servidor
def obtenerFirmas():
	global firmas
	return firmas

#Función que envía las detecciones del cliente al servidor
def enviarDetectados(detectados):
	# local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 12345

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# connect to server on local computer
	s.connect((host, port))

	# message you send to server
	message = "detectados"
	print(message)
	# message sent to server
	s.send(message.encode('ascii'))

	largo = len(detectados)
	textofinal = detectados[:largo - 1]

	# messaga received from server
	data = s.recv(1024)
	if (str(data.decode('ascii')) == "listo"):
		mensaje = str(socket.gethostbyname(socket.gethostname()))
		s.send(mensaje.encode('ascii'))
		data = s.recv(1024)

	if (str(data.decode('ascii')) == "esperando"):
		archivos = textofinal
		s.send(archivos.encode('ascii'))
	# close the connection
	s.close()

#Función main
def MainC():
    # local host IP '127.0.0.1'
	host = '127.0.0.1'

	# Define the port on which you want to connect
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# connect to server on local computer
	s.connect((host,port))

	# message you send to server
	message = "conectando"
	print(message)

	# message sent to server
	s.send(message.encode('ascii'))

	# messaga received from server
	data = s.recv(1024)
	if(str(data.decode('ascii')) == "conectado"):
		mensaje = str(socket.gethostbyname(socket.gethostname()))
		s.send(mensaje.encode('ascii'))

	#obtiene firmas
	data = s.recv(1024)
	firmasRecibidas = str(data.decode('ascii'))
	data = s.recv(1024)
	firmasRecibidas += str(data.decode('ascii'))

	global firmas
	firmas = firmasRecibidas.split(sep=',')

	# close the connection
	s.close()

#MainC()