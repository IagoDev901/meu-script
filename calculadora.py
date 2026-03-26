# calculadora.py

def calcular():
    print("Calculadora Python")
    
    try:
        # Entrada de dados
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /): ")
        num2 = float(input("Digite o segundo número: "))

        # Lógica das operações
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                return "Erro: Divisão por zero não é permitida!"
            resultado = num1 / num2
        else:
            return "Operação inválida!"

        return f"Resultado: {resultado}"

    except ValueError:
        return "Erro: Por favor, digite apenas números."

if __name__ == "__main__":
    print(calcular())
