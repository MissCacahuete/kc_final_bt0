from tkinter import *
from tkinter import ttk

_width = '900'
_lblwidth = 10
font = 'Verdana 10 bold'
_pady = 8
_padx = 4


def button(parent, text, ):
    btn = ttk.Button(parent, text=text)
    btn.grid(column=4, row=3, padx=55, pady=_pady)
    return btn


def label(parent, text, configuration):
    lbl = ttk.Label(parent, text=text, font=configuration.get('font', font), anchor=configuration.get('anchor', E),
                    width=configuration.get('width', _lblwidth), foreground=configuration.get('foreground', ''),
                    background=configuration.get('background', ''), relief=configuration.get('relief', ''))
    lbl.grid(column=configuration['col'], row=configuration['row'], padx=configuration.get('pad_x', _padx),
             pady=configuration.get('pad_y', _pady), columnspan=configuration.get('colspan', 1),sticky=configuration.get('sticky',''))

    return lbl


def entry(parent, text, variable, configuration):
    entry = ttk.Entry(parent, text=text, textvariable=variable, font=configuration.get('font', font),
                      width=configuration.get('width', _lblwidth), foreground=configuration.get('foreground', ''),
                      state=configuration.get('state', 'enable'), justify=configuration.get('justify', RIGHT))
    entry.grid(column=configuration.get('col'), row=configuration.get('row'))

    return entry


def label_without_text(parent, position):
    lbl = ttk.Label(parent, font=font, background='white', anchor=E, relief=GROOVE, width=22)
    lbl.grid(column=position['col'], row=position['row'], padx=_padx)
    return lbl
