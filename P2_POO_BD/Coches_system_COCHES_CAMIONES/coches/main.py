from re import match
from unittest import case

from coches import coches,cochesBD

class App:
    def __init__(self):
        self.main()

    def main(self):
        opcion=True
        while opcion: 
    
    def borrarPantalla(self):
        print("\033c")
    
    def espereTecla(self):
        input("...¡Oprima cualquier tecla para contunuar!...")

    def menu_acciones(self, tipo):
        print(f"\t\t....:::: M E N U   D E   {tipo} ::::...\n")
        opcion=input("\n\t1.- Agregar\n\t2.- Borrar\n\t3.- Modificar\n\t4.- Mostrar\n\t5.- Limpiar\n\t6.- Salir\n\t\tEscribe una opción: ").strip()
        return opcion   

    def respuesta(self,respuesta):
        if respuesta:
            input("...Accion Realizada con Exito...")
        else:
            input("...No fue posible realizar esta Accion intentalo nuevamente...")

    def datos_coche(selff,tipo):
        self.borrarPantalla()
        print(f"...Ingresar los datos del {tipo}")
        cochesito={}
        cochesito["marca"]=input("Marca:").upper().strip()
        cochesito["color"]=input("color:").upper().strip()
        cochesito["modelo"]=input("modelo:").upper().strip()
        cochesito["velocidad"]=input("velocidad").upper().strip()
        cochesito["potencia"]=input("potencia").upper().strip()
        cochesito["asientos"]=input("asientos").upper().strip()
        return cochesito
    


    def menu_coches(self):
        opc=True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case "1":
                    #crear un metodo que solicite los valores de los atributos de la clase y posteriormente crear un objeto de la clase coches y por ultimo enviar estos valores al objeto de la clase cochesBD
                    #crear objeto de cochesBD y luego insertar en la BD 
                    cochesito=self.datos_coche("coche")
                    coches1=coches.Coches(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velocidad"],cochesito["potencia"],cochesito["asientos"])

                    
                    cochesito1=cochesBD.CohesBD(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velocidad"],cochesito["potencia"],cochesito["asientos"])
                    respuesta=coches1.insertar()
                    self.respuesta(respuesta)
                    del coches1 
                case "2":
                    self.borrarPantalla()
                    id=input("ingrese el id que se va a borrar:").strip()
                    coches1=cochesBD.CochesBD("","","",0,0,0)
                    respuesta=coches1.eliminar(id)
                    self.respuesta(respuesta)
                    del coches1

                case "3":
                    self.borrarPantalla()
                    id=input("ingrese el id que se va a actualizar:").strip()
                    cochesito=self.datos_coche("coche")
                    cochesito1=cochesBD.CohesBD(cochesito["marca"],cochesito["color"],cochesito["modelo"],cochesito["velocidad"],cochesito["potencia"],cochesito["asientos"])
                    self.respuesta(respuesta)
                    del coches1
                case "4":
                    self.borrarPantalla()
                    coches1=cochesBD.CochesBD("","","",0,0,0)
                    registro=coches1.consultar()
                    num_coche1=1
                    if len (registro)
                    for fila in registro:
                        print(f"\n\tCoche#: {num_coche1}\n\t\tID: {fila[0]} \n\t\tmarca: {fila[1]} \n\t\tColor: {fila[2]} \n\t\tModelo: {fila[3]}  \n\t\tVelocidad: {fila[4]} \n\t\tPOTENCIA: {fila[5]}  \n\t\tAsientos: {fila[6]}")
                        num_coche1+=1
                        self.espereTecla()
                    else:
                        print("....No se encontro informacion de la BD....")
                        self.espereTecla()
                case "5":
                    pass
                case _:
                    self.opcionInvalida()
            del coches1

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=input("\n\t::::: MENU PRINCIPAL :::::\n\nCoches\n\nt2.- salir\n\n\tElige una opcion: ").lower().strip()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_coches()
                    self.esperarTecla()
                case "2":
                    self.borrarPantalla()
                    self.terminar()
                case _:
                    self.opcionInvalida()

if __name__=="__main__":
    app=App()