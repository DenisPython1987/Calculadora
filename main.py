import duploentry as du
import tkinter as tk
from tkinter import ttk
from calcular import Calcular


#Função para pegar os valores e apresentar o resultado
def executar(op):

    #Pega os valores da classe duploentry
    num1, num2 = frame.get_valores()
    if num1 is None or num2 is None:
        resultado_var.set("Erro: insira números válidos")
    else:
        resultado_var.set(Calcular.calcular(op, num1, num2))

#Inicia o programa
if __name__ == "__main__":

    #Cria a janela principal
    root = tk.Tk()
    root.title("Calculadora")

    #Cria o frame do resultado
    painel = ttk.LabelFrame(root, text='Resultado')
    painel.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    #Cria a variável que vai armazenar o resultado.
    resultado_var= tk.StringVar(value='0')

    #Cria o Label que vai mostrar o resultado
    resultado = ttk.Label(painel, textvariable=resultado_var)
    resultado.grid(row=0, column=0, sticky="nsew", ipadx=5, ipady=5)

    #Instancia a classe DuploInput
    frame = du.DuploInput(root)
    frame.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

    #Cria o Frame do teclado
    teclado = ttk.LabelFrame(root, text='Escolha uma operação:')
    teclado.grid(row=4, column=0, sticky=tk.W + tk.E, padx=5, pady=5)

    #Cria o teclado
    operações = ('+', '-', '*', '/')
    for i, op in enumerate(operações):
        ttk.Button(teclado, text=op, command=lambda o=op: executar(o)).grid(row=0,column=i, sticky='nsew', padx=5, pady=5)
    
  

    root.mainloop()
