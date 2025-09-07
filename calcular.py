"""Classe retirada do Chat GPT. Feita para realizar os cálculos matemáticos da
calculadora"""
class Calcular:
    """Classe simples para cálculos matemáticos"""

    #Define um método estático
    @staticmethod

    #Função para calcular os valores
    def calcular(op, num1, num2):
        operacoes = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else "Erro: Divisão por zero"
        }

        #Retorna operação inválida caso a operação esteja errada.
        return operacoes.get(op, lambda a, b: "Operação inválida")(num1, num2)
