# Proyecto1RedesEnLosNegocios

Este proyecto consiste en una estructura cliente-servidor que realiza una simulación de escaneo y detección de archivos peligrosos, como un antivirus.

## Software necesario para la modificación del proyecto

A continuación se listará el software que se utilizó para la elaboración del proyecto. Si desea utilizar otras versiones o programas, podría haber problemas de compatibilidad.

* Python 3.8
* PyCharm (Es un editor para archivos de Python y otros, pero se podría utilizar otro editor)
* MySql Server 8.0
* En caso de desear interfaz gráfica para utilizar Mysql -> MySQL Workbench 8.0 CE

## Pasos para instalar y modificar el proyecto

Primeramente se debe clonar este repositorio o bien, descargar el código comprimido.

Una vez descargado o clonado, para poder realizar cambios al proyecto es necesario utilizar un editor que permita modificar los archivos de extensión .py, para lo cual se utilizó PyCharm por las funcionalidades que provee para ejecutar Python.
Una vez abierto el proyecto y dentro de PyCharm, se debe verificar que se tenga un intérprete configurado tanto para el proyecto de servidor como para el de cliente. Para ello se debe proceder a la pestaña File -> Settings -> nombreDelProyecto -> Python Interpreter y, en caso de no tener uno, seleccionar un interprete de Python para el proyecto.
Seguidamente y en la misma ventana que se nos mostró para agregar el intérprete, a la extrema derecha se tiene un simbolo de "+" en el cual se pueden descargar e instalar librerías al proyecto. Para el servidor se requiere tener las siguientes librerías:
* EasyTkinter
* future
* mysql-connector-python
* pip
* protobuf
* setuptools
* six

Para el cliente se requieren las siguientes librerías:
* EasyTkinter
* future
* pip
* protobuf
* setuptools
* six

El siguiente paso consiste en la creación de la base de datos que utiliza el servidor.
Para ello se debe ejecutar MySQL Workbench o simplemente el shell de MySQL y ejecutar el script de la base de datos que se encuentra en el repositorio.

Una vez hecho todo lo anterior el usuario ya puede realizar los cambios que considere necesarios, iniciando con el archivo "Configuración" del proyecto Servidor, ya que este contiene las credenciales para el acceso al servidor de base de datos que se tiene para guardar los datos de la simulación.

## Setup Base de datos desde MySQL Workbench
Se abre MySQL Workbench 8.0 y se selecciona la opcion de agregar una nueva conexión. Una vez establecida la conexion se procede a crear la base de datos, donde solamente se tiene que tomar el documento bdProyecto1Redes.sql y ejecutarlo.

Una vez creada, se debe acceder a la carpeta del proyecto ServidorProyectoRedes, luego buscar y abrir el archivo Configuracion.py y cambiar las credenciales necesarias para que pueda realizar la conexión con la base de datos de acuerdo a la dirección, usuario, contraseña y puerto del servidor de base de datos que este utilizando.

## Ejecutar el proyecto
Para ejecutar el proyecto Servidor desde PyCharm, simplemente se da click derecho sobre el archivo "main.py" y se selecciona la opción "Run".

Para ejecutar el proyecto Cliente desde PyCharm, simplemente se da click derecho sobre el archivo "main.py" y se selecciona la opción "Run".

## Resultados
Una vez que se tienen los proyectos corriendo, el Servidor mostrará una ventana con 2 botones que permitirán mostrar tanto los clientes que se han conectado al servicio como los datos de los archivos que cada cliente ha detectado. 

Por otro lado, el cliente mostrará varias opciones para hacer posible la programación y la ejecución inmediata de los escaneos, también tendra la seccion donde muestra la ruta del directorio qe se va a escanear y en caso de programar el escaneo los datos que se utilizaran para realizarlo. Para descripciones más gráficas, acceda al manual de usuario.
