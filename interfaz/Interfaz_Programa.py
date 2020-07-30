from tkinter import *

class Interfaz_Programa:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Proyecto Bimestral")
        self.mi_frame = Frame(self.raiz, width="1500", height="1400")
        self.mi_frame.pack()  # si quiero que se configure el tamanio se hace con fill y para cambiar en y ademas de eso usar el parametro, expand = True
        self.mi_frame.config(bg='gray')
        self.crear_botones()
        self.iniciar_ventana()


    def boton_iniciar(self):
        exit()
        #aqui entraria la llamada al c[odigo que corre la deteccion de rostros

    def boton_ver_estadisticas(self):
        exit()
        #aqui entraria la llamada al c[odigo que corre la deteccion de rostros


    def boton_salir(self):
        exit()

    def crear_botones(self):
        boton_inicio = Button(self.mi_frame, text="Iniciar", command=self.boton_iniciar)
        boton_inicio.grid(row=3, column=1, pady=50, padx=10)
        boton_salir = Button(self.mi_frame, text="Salir", command = self.boton_salir)
        boton_salir.grid(row=3, column=3, pady=50, padx=10)
        boton_ver = Button(self.mi_frame, text="Estadisticas", command=self.boton_ver_estadisticas)
        boton_ver.grid(row=3, column=2, pady=50, padx=10)

    def iniciar_ventana(self):
        self.raiz.mainloop()
