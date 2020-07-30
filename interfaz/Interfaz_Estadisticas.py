from tkinter import *

class Interfaz_Estadisticas:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Proyecto Bimestral - Estadisticas")
        self.mi_frame = Frame(self.raiz)
        self.mi_frame.pack()  # si quiero que se configure el tamanio se hace con fill y para cambiar en y ademas de eso usar el parametro, expand = True
        self.mi_frame.config(bg='gray')
        self.crear_botones()
        self.crear_labels()
        self.iniciar_ventana()

    def boton_salir(self):
        exit()

    def crear_labels(self):
        self.label_titulo = Label(self.mi_frame, text="Estadísticas", font =('Arial',24))
        self.label_titulo.grid(row=1, column=2, pady=10)
        self.label_feliz = Label(self.mi_frame, text="Sentimiento de Felicidad: ")
        self.label_feliz.grid(row=2, column=2, pady=10)
        self.label_enojado = Label(self.mi_frame, text="Sentimiento Enojo: ")
        self.label_enojado.grid(row=4, column=2, pady=10)

    def crear_botones(self):
        boton_salir = Button(self.mi_frame, text="Salir", command = self.boton_salir)
        boton_salir.grid(row=6, column=2, pady=50)

    def iniciar_ventana(self):
        self.raiz.mainloop()
