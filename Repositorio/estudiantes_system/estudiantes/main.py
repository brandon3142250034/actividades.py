from estudiantes import Estudiantes
from tkinter import Tk, Label,Entry,Button,messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de Estudiantes")
        self.ventana.geometry("600x600")
        self.main()

    def respuesta(self,respuesta):
        if respuesta:
           messagebox.showinfo(title="Exitoso", message="Accion realizada con exito")
        else:
           messagebox.showerror(title="Verifique porfavor", message="Esta accion no pudo realizarse en este momento")

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    def menu_acciones(self, tipo):
        self.borrarPantalla()
        tipo="estudiante"
        Label(self.ventana,text=f"....:::: M E N U   D E   {tipo} ::::..").pack(pady=10)
        Button(self.ventana,text="1.- Agregar",command=self.insertar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_estudiante_view).pack(pady=10)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=10)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text="::: Menu Principal :::, ",).pack(pady=20)
        Button(self.ventana,text="1.-Estudiantes",command=lambda: self.menu_acciones("Estudiante")).pack(pady=10)
        Button(self.ventana,text="2.-salir",command=self.ventana.quit).pack(pady=10)

    def insertar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=f"....:::: Ingresar los datos del estudiante ::::..").pack(pady=10)

        Label(self.ventana,text="Nombre:").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Nota:").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text=":::Agregar:::",command=self.insertar_estudiante_controller).pack(pady=5)

    def insertar_estudiante_controller(self):
        estudiantes1=Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiantes1.insertar()
        self.respuesta(respuesta)
        del estudiantes1

    def eliminar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=f"....:::: Ingresar el id del estudiante que va a eliminar ::::..").pack(pady=10)

        Label(self.ventana,text="ID:").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)   

        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text=":::Eliminar:::",command=self.eliminar_estudiante_controller).pack(pady=5)

    def eliminar_estudiante_controller(self):
        estudiantes1=Estudiantes()
        respuesta=estudiantes1.eliminar(self.id.get())
        self.respuesta(respuesta)
        del estudiantes1

    def consultar_estudiante_controller(self,filas):
        registros=Estudiantes.consultar()
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"\n\t estudiante #: {num_estudiante} \n\t ID: {fila[0]} \n\t Nombre: {fila[1]} \n\t Nota: {fila[2]} \n" 
                num_estudiante+=1
        else:
            filas="no se encontro infromacion en la BD..."
        return filas

    def modificar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=f"....:::: Ingresar el id del estudiante que va a modificar ::::..").pack(pady=10)

        Label(self.ventana,text="ID:").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)   

        Label(self.ventana,text=f"....:::: datos del estudiante ::::..").pack(pady=10)
        
        Label(self.ventana,text="Nombre:").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Nota:").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text=":::Modificar:::",command=self.modificar_estudiante_controller).pack(pady=5)

    def modificar_estudiante_controller(self):
        id=self.id.get()
        estudiantes1=Estudiantes.Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiantes1.actualizar(id)
        self.respuesta(respuesta)
        del estudiantes1

    def consultar_estudiante_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="..:: Consultar estudiantes ::..").pack(pady=10)
        filas=""
        filas=self.consultar_estudiante_controller(filas)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Button(self.ventana,text=":::Regresar:::",command=self.menu_acciones).pack(pady=5)

if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)    
    #app=App()
    ventana.mainloop()