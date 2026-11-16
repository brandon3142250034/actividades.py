from coches import Coches, coches
from tkinter import Tk, Label,Entry,Button
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("600x600")
        self.main()
    
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def menu_acciones(self, tipo):
        self.borrarPantalla()
        tipo="coche"
        Label(self.ventana,text=f"....:::: M E N U   D E   {tipo} ::::..").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_coches_biew).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_coche_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_coche_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_coche_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=10)
    
    def respuesta(self,respuesta):
        if respuesta:
           messagebox.showinfo(title="Exitoso", message="Accion realizada con exito")
        else:
           messagebox.showerror(title="Verifique porfavor", message="Esta accion no pudo realizarse en este momento")
            
    def insertar_coches_biew(self):
        self.borrarPantalla()
        Label(self.ventana,text=f"....:::: Ingresar los datos del coche ::::..").pack(pady=10)
        
        Label(self.ventana,text="Marca:").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color:").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo:").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad:").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia:").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Asientos:").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text=":::Agregar:::",command=self.insertar_coche_controller).pack(pady=5)
         
    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text="::: Menu Principal :::, ",).pack(pady=20)
        Button(self.ventana,text="1.-coches",command=self.insertar_coches_biew).pack(pady=10)
        Button(self.ventana,text="2.-salir",command=self.ventana.quit).pack(pady=10)

    def consultar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="..:: Consultar coches ::..").pack(pady=10)
        filas=""
        filas=self.consultar_coche_controller(filas)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)

    def insertar_coche_controller(self):
        coches1=coches,Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.insetar()
        self.respuesta(respuesta)
        del coches1

    def eliminar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=f"....:::: Ingresar el id del coche que va a eliminar ::::..").pack(pady=10)

        Label(self.ventana,text="ID:").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)   

        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text=":::Eliminar:::",command=self.eliminar_coche_controller).pack(pady=5)

    def eliminar_coche_controller(self):
        coches1=coches,Coches()
        respuesta=coches1.eliminar(self.id.get())
        self.respuesta(respuesta)
        del coches1

    def consultar_coche_controller(self,filas):
        registros=coches.Coches.consultar()
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"\n\t coche #: {num_coche} \n\t ID: {fila[0]} \n\t Marca: {fila[1]} \n\t Color: {fila[2]} \n\t Modelo: {fila[3]} \n\t Velocidad: {fila[4]} \n\t Potencia: {fila[5]} \n\t Asientos: {fila[6]} \n" 
                num_coche+=1
        else:
            filas="no se encontro infromacion en la BD..."
        return filas

    def modificar_coche_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=f"....:::: Ingresar el id del coche que va a modificar ::::..").pack(pady=10)

        Label(self.ventana,text="ID:").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)   

        Label(self.ventana,text=f"....:::: datos del coche ::::..").pack(pady=10)
        
        Label(self.ventana,text="Marca:").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana,text="Color:").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana,text="Modelo:").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana,text="Velocidad:").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana,text="Potencia:").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Asientos:").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text=":::Modificar:::",command=self.modificar_coche_controller).pack(pady=5)

    def modificar_coche_controller(self):
        id=self.id.get()
        coches1=coches,Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coches1.actualizar(id)
        self.respuesta(respuesta)
        del coches1

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)    
    #app=App()
    ventana.mainloop()