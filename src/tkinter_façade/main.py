from tkinter import *

from src.tkinter_façade.conversor import Conversor


class Tkinter(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.geometry("920x600")
        self.title("Cryptonedas")
        self.resizable(0,0)
        self.simulador = Conversor(self)
        self.simulador.place(x=0, y=0)
       
    def start(self):
        self.mainloop()