import mysql.connector


class Registro_datos():
    def __init__(self):
        self.conexion = mysql.connector.connect( host='localhost',
                                            database ='base_datos', 
                                            user = 'root',
                                            password ='admin')
    def inserta_producto(self,numero, nombre, unidad, puesto):
        cur = self.conexion.cursor()
        sql='''INSERT INTO productos (NUMERO, NOMBRE, UNIDAD, PUESTO) 
        VALUES('{}', '{}','{}', '{}')'''.format(numero, nombre, unidad, puesto)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()
    def buscar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM productos " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_producto(self, numero_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM productos WHERE NUMERO = {}".format(numero_producto)
        cur.execute(sql)
        numerox = cur.fetchall()
        cur.close()     
        return numerox

    def elimina_productos(self,numero):
        cur = self.conexion.cursor()
        sql='''DELETE FROM productos WHERE NUMERO = {}'''.format(numero)
        cur.execute(sql)
        nom = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return nom   
    def actualiza_productos(self, numero, nombre, unidad, puesto):
        cur = self.conexion.cursor()
        sql ='''UPDATE productos SET  NOMBRE ='{}' , UNIDAD = '{}', PUESTO = '{}'
        WHERE NUMERO = '{}' '''.format( nombre,  unidad, puesto, numero)
        cur.execute(sql)
        act = cur.rowcount
        self.conexion.commit()    
        cur.close()
        return act  
