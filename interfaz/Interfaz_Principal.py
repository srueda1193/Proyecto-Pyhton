from tkinter import *
from Interfaz_Formulario import Interfaz_Formulario

class Interfaz_Principal:

    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Proyecto Bimestral")
        self.raiz.config(bg="black")
        self.mi_frame = Frame(self.raiz, width="500", height="400")
        self.mi_frame.pack()  # si quiero que se configure el tamanio se hace con fill y para cambiar en y ademas de eso usar el parametro, expand = True
        self.mi_frame.config(bg='gray')
        self.crear_labels()
        self.crear_botones()
        self.iniciar_ventana()

    # creacion de labels
    def crear_labels(self):
        label_bienvenidos = Label(self.mi_frame, text="Bienvenidos", font=("Arial", 48))
        label_bienvenidos.grid(row=1, column=1, pady=10)
        label_subtitulo = Label(self.mi_frame, text="Proyecto Bimestral\nIdentificador de Rostros", font=("Roboto", 18))
        label_subtitulo.grid(row=2, column=1, pady=10)

    def boton_continuar(self):
        Interfaz_Formulario()

    def crear_botones(self):
        boton_conti = Button(self.mi_frame, text="Continuar", command=self.boton_continuar)
        boton_conti.grid(row=3, column=1, pady=50)

    def iniciar_ventana(self):
        self.raiz.mainloop()


if __name__ == '__main__':
    Interfaz_Principal()









