#Classe para calcular os valores

class Calcular:
    """Classe simples para cálculos matemáticos"""

    @staticmethod
    def calcular(op, num1, num2):
        operacoes = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else "Erro: Divisão por zero"
        }
        return operacoes.get(op, lambda a, b: "Operação inválida")(num1, num2)
