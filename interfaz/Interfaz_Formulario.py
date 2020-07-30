from tkinter import *
from Interfaz_Programa import Interfaz_Programa

class Interfaz_Formulario:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Proyecto Bimestral - Login")
        self.mi_frame = Frame(self.raiz, width="500", height="400")
        self.mi_frame.pack()  # si quiero que se configure el tamanio se hace con fill y para cambiar en y ademas de eso usar el parametro, expand = True
        self.mi_frame.config(bg='gray')
        self.crear_labels()
        self.crear_botones()
        self.crear_cuadros()
        self.iniciar_ventana()

    def crear_labels(self):
        self.label_nombre = Label(self.mi_frame, text="Nombre: ")
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)
        self.label_contrasenia = Label(self.mi_frame, text="Contraseña: ")
        self.label_contrasenia.grid(row=1, column=0, padx=10, pady=10)

    # creacion de cuadros de entrada de texto
    def crear_cuadros(self):
        self.cuadro_nombre = Entry(self.mi_frame)
        self.cuadro_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.cuadro_contrasenia = Entry(self.mi_frame)
        self.cuadro_contrasenia.grid(row=1, column=1, padx=10, pady=10)

    def boton_continuar(self):
        self.verificar_credenciales()

    def verificar_credenciales(self):

        if(self.cuadro_nombre.get() == 'sebas' and self.cuadro_contrasenia.get() == '1234'):
            Interfaz_Programa()
        else:
            print("Las credenciales no son correctas")
            self.iniciar_ventana()

    def boton_salir(self):
        exit()

    def crear_botones(self):
        boton_conti = Button(self.mi_frame, text="Continuar", command=self.boton_continuar)
        boton_conti.grid(row=3, column=1, pady=50)
        boton_salir = Button(self.mi_frame, text="Salir", command = self.boton_salir)
        boton_salir.grid(row=3, column=2, pady=50)

    def iniciar_ventana(self):
        self.raiz.mainloop()
