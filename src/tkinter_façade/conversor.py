from tkinter import *
from tkinter import ttk

from src.tkinter_façade import movement
from tkinter_façade.results import Results
from tkinter_façade.transaction import Transaction


_width='900'

class Conversor(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, width='900', height='600')
        self.new_transaction_btn = ttk.Button(self, text ='Nueva transacción', command=lambda: self.new_transaction_conversor(), width=18)
        self.new_transaction_btn.place(x=600, y=233)

        self.clear_button = ttk.Button(self, text='Clear', command=lambda: self.clear_transactions(),
                                  width=15)
        self.clear_button.place(x=740, y=233)

        self.movements =movement.Movement(self, height=240, width= _width)
        self.movements.place(x=20,y=20)

        self.newTransaction= Transaction(self, height=220, width=_width)
        self.newTransaction.place(x=40, y=260)

        self.results = Results(self, height=100, width=_width)
        self.results.place(x=40, y=500)

    def print_movements(self):
        self.movements.print_movements()
        self.movements.update_scroll_view()
           
    def new_transaction_conversor(self):
        self.newTransaction.switchNewTransaction(TRUE)
        self.results.resetLabels()

    def clear_transactions(self):
        self.movements.clear_movements()