import duploentry as du
import tkinter as tk
from tkinter import ttk
from calcular import Calcular

def executar(op):
    num1, num2 = frame.get_valores()
    if num1 is None or num2 is None:
        resultado_var.set("Erro: insira números válidos")
    else:
        resultado_var.set(Calcular.calcular(op, num1, num2))
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Exemplo DuploInput")

    painel = ttk.LabelFrame(root, text='Resultado')
    painel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    resultado_var= tk.StringVar(value='0')
    resultado = ttk.Label(painel, textvariable=resultado_var)
    resultado.grid(row=0, column=0, sticky="nsew", ipadx=5, ipady=5)

    frame = du.DuploInput(root)
    frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    
    teclado = ttk.LabelFrame(root, text='Escolha uma operação:')
    teclado.grid(row=4, column=0, sticky=tk.W + tk.E, padx=5, pady=5)

    operações = ('+', '-', '*', '/')
    for i, op in enumerate(operações):
        ttk.Button(teclado, text=op, command=lambda o=op: executar(o)).grid(row=0,column=i, sticky='nsew', padx=5, pady=5)
    
  

    root.mainloop()
