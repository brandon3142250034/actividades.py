
print("\033c")
class Coches:
    def __init__(self, marca="", color="", modelo="", velocidad=0, potendcia=0, asientos=0):
        self._marca = marca
        self._color = color
        self._modelo = modelo
        self._velocidad = velocidad
        self._potencia = potendcia
        self._asientos = asientos


    def acelerar(self):
        self._velocidad+=1
        print(f"ahora la velocidad es: {self._velocidad}")

    def frenar(self):
        self._velocidad-=1
        print(f"ahora la velocidad es: {self._velocidad}")

    def getVelocidad(self):
        return self._velocidad

    def setVelocidad(self,velocidad):
        self._velocidad = velocidad 

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getColor(self):
        return self._color

    def setColor(self,color):
        self._color = color

    def getModelo(self):
        return self._modelo

    def setModelo(self, modelo):
        self._modelo = modelo

    def getPotencia(self):
        return self._potencia

    def setPotencia(self, potencia):
        self._potencia = potencia

    def getAsientos(self):
        return self._asientos

    def setAsientos(self, asientos):
        self._asientos = asientos

    def __init__(self,marca,color,modelo,velocidad,potencia,asientos,eje,CapacidadCarga,tipo_carga):
        super().__init__(marca,color,modelo,velocidad,potencia,asientos,eje,CapacidadCarga)
        self.__tipo_carga=tipo_carga

    def acelerar(self):
        self._velocidad+=1
        print(f"Estoy acelerando como un camion de carga {self._velocidad}")

    def frenar(self):
        self._velocidad-=1
        print(f"Estoy frenando como un camion de carga {self._velocidad}")

    def getTipo_Carga(self):
        return self.__tipo_carga

    def setTipo_Carga(self,tipo_carga):
        self.__tipo_carga=tipo_carga




