import pymysql.cursors

def conectar():
    connection = pymysql.connect(
        host='srv1718.hstgr.io', # conexin a servidor de recurso
        user='u208593669_Blazkull_777', # usuario de conexion a mysql
        password='FinanzaCul777!',# clave de la conexion a la mysql
        database='u208593669_Finanzas_perso',# nombre de base de datos
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection
