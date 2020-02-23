from datetime import datetime as dt
from tkinter import *
from tkinter import ttk

from api import convert_coins
from constants import NEW_TRANSACTION
from domain.movement import Movement
from repository.cryptos_repository import get_cryptos
from repository.movements_repository import insert_movement
from tkinter_façade.facçade import label, entry

_width = 812
_lblwidth = 10
font = 'Verdana 10 bold'
_pady = 8
_padx = 4


class Transaction(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, height=210, width=_width, borderwidth=2, relief=GROOVE)
        self.conversor = parent

        self.strFrom_Q = StringVar(value='')
        self.strOldFrom_Q = self.strFrom_Q.get()
        self.strFrom_Q.trace('w', self.entryValidationFrom)

        self.getFromCrypto = StringVar()
        self.getToCrypto = StringVar()

        self.init_labels()

        self.up_lbl = label(self, '', {'col': 3, 'row': 3, 'width': 22, 'background': 'whitesmoke', 'relief': GROOVE})
        self.toq_lbl = label(self, '', {'col': 3, 'row': 2, 'width': 22, 'background': 'whitesmoke', 'relief': GROOVE})
        self.errors_lbl = label(self, '', {'col': 0, 'row': 4, 'colspan': 5, 'font': 'Verdana 8', 'anchor': CENTER,
                                           'foreground': 'red', 'width': 40})
        self.fq_entry = entry(self, '', self.strFrom_Q,
                              {'col': 1, 'row': 2, 'width': 22, 'justify': RIGHT, 'state': 'disable'})

        self.init_combos()

        self.init_buttons()

    def init_buttons(self):
        self.calculateButton = ttk.Button(self, text='Calcular', command=lambda: self.calculateTransaction(),
                                          state='disable')
        self.calculateButton.grid(column=4, row=1, padx=60, pady=_pady)
        self.cancelButton = ttk.Button(self, text='Cancelar', command=lambda: self.switchNewTransaction(FALSE, TRUE),
                                       state='disable')
        self.cancelButton.grid(column=4, row=2, padx=30, pady=_pady)
        self.checkButton = ttk.Button(self, text='Aceptar', command=lambda: self.calculateTransaction(TRUE),
                                      state='disable')
        self.checkButton.grid(column=4, row=3, padx=30, pady=_pady)

    def init_combos(self):
        self.cryptos = get_cryptos()
        self.fromCryptoCombo = ttk.Combobox(self, width=20, font=font, textvariable=self.getFromCrypto,
                                            values=[it.name for it in self.cryptos],
                                            state='disable')
        self.fromCryptoCombo.grid(column=1, row=1)
        self.toCryptoCombo = ttk.Combobox(self, width=20, font=font, textvariable=self.getToCrypto,
                                          values=[it.name for it in self.cryptos],
                                          state='disable')
        self.toCryptoCombo.grid(column=3, row=1)

    def init_labels(self):
        label(self, NEW_TRANSACTION,
              {'col': 0, 'row': 0, 'width': 20, 'anchor': CENTER, 'pad_x': 2, 'pad_y': 20, 'colspan': 2, 'sticky': W})
        label(self, 'From:', {'col': 0, 'row': 1})
        label(self, 'Q:', {'col': 0, 'row': 2})
        label(self, 'To:', {'col': 2, 'row': 1})
        label(self, 'Q:', {'col': 2, 'row': 2})
        label(self, 'U.P:', {'col': 2, 'row': 3})


    def select_crypto(self, event):
        self.calculateButton.config(state='enable')
        self.errors_lbl.config(text=' ')

    def strCleaner(self):
        strcleaned = ''
        for i in range(len(self.strFrom_Q.get())):
            if self.strFrom_Q.get()[i] != ' ':
                strcleaned += self.strFrom_Q.get()[i]
        return (strcleaned)

    def entryValidationFrom(self, *args):
        if self.strFrom_Q.get() == '':
            self.strOldFrom_Q = self.strFrom_Q.get()
        else:
            try:
                self.floatFrom_Q = float(self.strFrom_Q.get())
                self.strFrom_Q.set(self.strCleaner())
                self.strOldFrom_Q = self.strFrom_Q.get()
                self.calculateButton.config(state='enable')
                self.errors_lbl.config(text=' ')
            except:
                self.strFrom_Q.set(self.strOldFrom_Q)

    def calculateTransaction(self, insert=FALSE):
        from_currency = [it.symbol for it in self.cryptos if it.name == self.getFromCrypto.get()][0]
        quantity = self.strFrom_Q.get()
        to_currency = [it.symbol for it in self.cryptos if it.name == self.getToCrypto.get()][0]
        if from_currency != to_currency:
            conversion = convert_coins(quantity, from_currency, to_currency)
            now = dt.now()
            self.movement = Movement(None, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"), from_currency, quantity,
                                     to_currency, conversion.calculate_amount())
            self.toq_lbl.config(text=self.movement.to_quantity)
            self.up_lbl.config(text=self.movement.unitary_price())
            if insert == TRUE:
                insert_movement(self.movement)
                self.conversor.print_movements()
            return True
        else:
            self.errors_lbl.config(text="No puede ser la misma moneda")
            return False

    def switchNewTransaction(self, switch_On=FALSE, transactionButton=FALSE):
        if switch_On:
            switch_state = 'enable'
            colorbg = 'white'
            switch_combo = 'readonly'
        else:
            switch_state = 'disable'
            colorbg = 'whitesmoke'
            switch_combo = 'disable'

        self.up_lbl.config(background=colorbg)
        self.toq_lbl.config(background=colorbg)
        self.fq_entry.config(state=switch_state)
        self.fromCryptoCombo.config(state=switch_combo)
        self.toCryptoCombo.config(state=switch_combo)
        self.cancelButton.config(state=switch_state)
        self.calculateButton.config(state=switch_state)
        self.checkButton.config(state=switch_state)

        if transactionButton:
            self.variable_reset()

    def variable_reset(self):
        self.errors_lbl.config(text='')
        self.toCryptoCombo.set('')
        self.fromCryptoCombo.set('')
        self.toq_lbl.config(text='')
        self.up_lbl.config(text='')
        self.cryptoInvertida = 0
        self.strOldFrom_Q = ''
        self.strFrom_Q.set(self.strOldFrom_Q)
