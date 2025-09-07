#Biblioteca de funções
import tkinter as tk
from tkinter import ttk
    
class DuploInput(tk.Frame):
    """Uma classe para personalizar a classe Frame com dois Entry"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label1 = ttk.Label(self, text='Digite o primeiro número')
        self.label1.grid(row=1, column=0, sticky=tk.W + tk.E, padx=5, pady=5)

        self.entry1 = ttk.Entry(self)
        self.entry1.grid(row=1, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        self.label2 = ttk.Label(self, text='Digite o segundo número')
        self.label2.grid(row=2, column=0, sticky=tk.W + tk.E, padx=5, pady=5)

        self.entry2 = ttk.Entry(self)
        self.entry2.grid(row=2, column=1, sticky=tk.W + tk.E, padx=5, pady=5)

        self.columnconfigure(1, weight=1)

    def get_valores(self):
            """Retorna os valores digitados como strings"""
            try:
                return float(self.entry1.get()), float(self.entry2.get())
            except ValueError:
                 return None, None  
 