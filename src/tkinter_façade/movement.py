from tkinter import *
from tkinter import ttk

from repository.movements_repository import list_movements, clear_movement


class Movement(ttk.Frame):
    _table_header = ['Date', 'Time', 'From', 'Quantity', 'To', 'Quantity', 'UnitaryPrice']

    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, height=kwargs['height'], width=kwargs['width'])
        self.labels = []

        self.print_table_headers()

        self.table_frame = Frame(self, bd=2, relief=GROOVE)
        self.table_frame.grid(column=0, row=1, columnspan=8)

        self.scrollbar = Scrollbar(self.table_frame)
        self.scrollbar.grid(row=0, column=1, sticky=N + S)
        self.scrollbar.grid_columnconfigure(1, weight=1)
        self.canvas = Canvas(self.table_frame, yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=0, column=0, sticky=N + S + E + W)
        self.canvas.config(width=810, height=180)
        self.canvas.grid_propagate(0)
        self.scrollbar.config(command=self.canvas.yview)

        self.init_frame()

        self.windows = self.canvas.create_window(0, 0, anchor=NW, window=self.frame)

        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def init_frame(self):
        self.frame = Frame(self.canvas, width=810, height=180)
        self.print_movements()

    def print_table_headers(self):
        for index, header in enumerate(self._table_header, start=0):
            self.lblDisplay = ttk.Label(self, text=header, font='verdana, 10', width=16, background='white',
                                        borderwidth=1, relief=GROOVE, anchor=CENTER)
            self.lblDisplay.grid(row=0, column=index, pady=1)
            self.lblDisplay.grid_propagate(0)
        self.lblDisplay = ttk.Label(self, font='verdana, 10', width=2)
        self.lblDisplay.grid(row=0, column=7, pady=1)
        self.lblDisplay.grid_propagate(0)

    def update_scroll_view(self):
        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def print_movements(self):
        self.movements = list_movements()
        for i, movement in enumerate(self.movements, start=0):
            keys = [key for key in movement.__dict__.keys() if key != 'id']
            for j, attr in enumerate(keys, start=0):
                self.labels.append(self.movement_label(movement.__getattribute__(attr), i, j))
                if (j == len(keys) - 1):
                    self.labels.append(self.movement_label(movement.unitary_price(), i, j + 1))
        self.canvas.config(scrollregion=self.canvas.bbox('all'))

    def clear_movements(self):
        clear_movement()
        for label in self.labels: label.destroy()
        self.print_movements()
        self.update_scroll_view()

    def movement_label(self, text, row, column):
        self.lblDisplay = ttk.Label(self.frame, text=text, font='Verdana, 10',
                                    width=16, background='white',
                                    borderwidth=1, relief=GROOVE, anchor=CENTER)
        self.lblDisplay.grid(row=row, column=column)
        self.lblDisplay.grid_propagate(0)
        return self.lblDisplay
