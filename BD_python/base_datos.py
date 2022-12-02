import mysql.connector
from mysql.connector import Error

#Metodo init se ejecutará cuando mande a llamar la clase BD
class BD():
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(host = "localhost", user = "root", passwd='rootroot',db = "bdPendientes")
            ##self.conexion = mysql.connector.connect(host = "localhost", user = "root", password = "", db = "bdpendientes")    
        except Error as ex:
            print("Error al intentar la conexión es: {0}".format(ex))
    
    def select(self, tabla):
        if self.conexion.is_connected():
            try:
                script = "SELECT * FROM " + tabla
                cursor = self.conexion.cursor()
                cursor.execute(script)
                consulta = cursor.fetchall()
                return consulta
            except Error as ex:
                print("Error al intentar la conexión es: {0}".format(ex))
    
    def eliminar(self, sentencia):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(sentencia)
            except Error as ex:
                print("Error al intentar la conexión es: {0}".format(ex))

