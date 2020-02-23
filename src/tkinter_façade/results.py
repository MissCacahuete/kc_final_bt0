from tkinter import *
from tkinter import ttk

from api import convert_coins
from repository.movements_repository import list_movements
from tkinter_façade.facçade import label, label_without_text, button

_width = '900'
_lblwidth = 10
font = 'Verdana 10 bold'
_pady = 8
_padx = 4


class Results(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, height=kwargs['height'], width=kwargs['width'])

        label(self, 'Inversion €', {'col': 0, 'row': 3})
        label(self, 'Valor actual', {'col': 2, 'row': 3})

        self.euros_label = label_without_text(self, {'col': 1, 'row': 3})
        self.investments_label = label_without_text(self, {'col': 3, 'row': 3})
        self.calculate_investment_button = button(self, 'Calcular').configure(command= lambda: self.investments())

    def investments(self):
        movements = list_movements()
        eur = 0
        cryptos = dict()
        for it in movements:
            (eur, cryptos) = self.accumulated_currency(cryptos, eur, it, 'from_currency', 'from_quantity')
            (eur, cryptos) = self.accumulated_currency(cryptos, eur, it, 'to_currency', 'to_quantity')

        cr_amount = 0
        for crypto in cryptos:
            cr_amount += convert_coins(cryptos[crypto], crypto, 'EUR').price

        self.euros_label.config(text=eur)
        self.investments_label.config(text=cr_amount)

    def accumulated_currency(self, cryptos, eur, it, currency, amount):
        if it.__getattribute__(currency) == 'EUR':
            eur += it.__getattribute__(amount)
        else:
            try:
                cryptos[it.__getattribute__(currency)] += it.__getattribute__(amount)
            except KeyError:
                cryptos[it.__getattribute__(currency)] = it.__getattribute__(amount)
        return [eur, cryptos]

    def resetLabels(self):
        # Cuando se quiere hacer un nuevo movimiento se resetean las labels de resultado
        self.euros_label.config(text='')
        self.investments_label.config(text='')
