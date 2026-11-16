from Lib import re

from Coches_system.coches import conexionBD

from conexionBD import mysql,cursor

class cochesBD:
    def __init__(self,marca,color,modelo,velocidad,potencia,asientos):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._potencia=potencia
        self._asientos=asientos

    def insertar(self):
        try:
            cursor.execute("insert into coches values (null,%s,%s,%s,%s,%s,%s)",(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos))
            conexionBD.commit()
            return True
        except:
            return False

    def consultar(self):
        try:
            cursor.execute("select * from coches")
            return ["Algo"]
        except:
            return []
   
    def eliminar(self,id):
        try:
            cursor.execute("detele from coches where id=%s"(id,))
            conexionBD.commit()
            return True
        except:
            return False 

    def actualizar(self,id):
        try:
            cursor.execute("detele from coches where id=%s"(self._marca,self._color,self._modelo,self._velocidad,self._potencia,self._asientos,id))
            conexionBD.commit()
            return True
        except:
            return False