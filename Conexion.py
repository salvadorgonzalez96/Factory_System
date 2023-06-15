import pymysql


class Conexion:
    def getConexion(self):
        conexion = pymysql.connect(
          host="localhost",
          user="root",
          password="gonzalez",
          database="mydb",
          cursorclass=pymysql.cursors.DictCursor

        )
        return conexion
    
