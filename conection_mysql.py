import pymysql.cursors

def conectar():
    connection = pymysql.connect(
        host='localhost', # conexin a servidor de recurso
        user='root', # usuario de conexion a mysql
        password='1234',# clave de la conexion a la mysql
        database='finanza_personal',# nombre de base de datos
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
