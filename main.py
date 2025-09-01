#Calculadora
import tkinter as tk
from tkinter import ttk

def adicionar_numero(num):
    """Adiciona o número pressionado ao texto atual"""
    valor_atual = resultado_var.get()
    if valor_atual == '0':
        resultado_var.set(str(num))
    else:
        resultado_var.set(valor_atual + str(num))

#Aqui eu crio a janela principal
root = tk.Tk()

#Aqui eu determino o tamamnho e a posição da janela
root.geometry('500x300+300+300')

#Aqui eu determino o título da janela
root.title('Calculadora')

#Aqui eu determino que a calculadora não pode ser redimensionada
root.resizable(False, False)

#Aqui eu crio o painel onde será mostrada a janela
mostrador = ttk.Labelframe(root, text='Resultado')
mostrador.grid(row=0, column=0, columnspan=10, sticky='nsew')
mostrador.columnconfigure(0, weight=10)

#Aqui eu crio o Label que vai mostrar o resultado
resultado_var = tk.StringVar(value='0')
painel = tk.Label(mostrador, textvariable=resultado_var)
painel.grid(row=0, column=0, sticky=tk.E)

#Aqui eu crio um frame para o teclado
teclado = tk.Frame(root)

#Aqui eu coloco o grid em quatro colunas e três linhas
teclado.grid(row=2, column=0, rowspan=3, columnspan=4, sticky="nsew")

for i in range(1, 10):
    botão = tk.Button(teclado, text=str(i), command=lambda num=i:adicionar_numero(num))
    linha = ((i - 1) // 3) + 1
    coluna = (i - 1) % 3
    botão.grid(row=linha, column=coluna, pady=5, padx=5)

botão_0 = tk.Button(teclado, text='0', width=15, command=lambda: adicionar_numero("0"))
botão_0.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()