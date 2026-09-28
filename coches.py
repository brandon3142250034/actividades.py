"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.
"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")
class Coches:
    def _init_(self, marca="", color="", modelo="", velocidad=0, caballaje=0, plazas=0):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    def acelerar(self):
        self.velocidad += 1
        print(f"Ahora la velocidad es: {self.velocidad}")

    def frenar(self):
        self.velocidad -= 1
        print(f"Ahora la velocidad es: {self.velocidad}")


# Creación de los objetos según el diagrama
coche1 = Coches(
    marca="VW",
    color="Blanco",
    modelo="2022",
    velocidad=220,
    caballaje=150,
    plazas=5
)

coche2 = Coches(
    marca="Nissan",
    color="Azul",
    modelo="2020",
    velocidad=180,
    caballaje=150,
    plazas=6
)

# Pruebas
print(f"El coche 1 es de color: {coche1.color}")
print(f"El coche 2 es de color: {coche2.color}")

print("\n--- Acelerando coche1 ---")
for i in range(1, 11):
    coche1.acelerar()

print("\n--- Frenando coche1 ---")
for i in range(1, 6):
    coche1.frenar()