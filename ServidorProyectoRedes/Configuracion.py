from re import error
import mysql.connector

#connection to sql server

_mysql_server = 'localhost'#nombre del servidor local
_mysql_database= 'bdRedes'
_mysql_server_port = 3306
_mysql_user = "root"
_mysql_paswword = "12345"

#SQL SERVER CONNECTION FUNC
def mysql_connection():
    try:
        cnx = mysql.connector.connect( host=_mysql_server, user= _mysql_user, passwd=_mysql_paswword, db=_mysql_database )
        return cnx
    except:
        print('ERROR: MySQL Connection')

#CALL STORED PROCEDURES FROM SQL SERVER

def get_data_from_sql(sp):
    try:
        con = mysql_connection()
        cur = con.cursor()
        cur.execute(sp)
        data_return = cur.fetchall()
        con.commit()

        return data_return
    except error as e:
        print("Error: {0} Getting dat from MSSQL: {1}".format(
            e.errno, e.sterror))


def set_data_from_sql(sp):
    try:
        con = mysql_connection()
        cur = con.cursor()
        cur.execute(sp)
        con.commit()

    except error as e:
        print("Error: {0} Setting dat from MSSQL: {1}".format(
            e.errno, e.sterror))