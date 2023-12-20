def calculadora(num1, num2, operacao):
    if operacao == 1:
        soma = num1 + num2
        return soma
    elif operacao == 2:
        subtracao = num1 - num2
        return subtracao
    elif operacao == 3:
        multiplicacao = num1 * num2
        return multiplicacao
    elif operacao == 4:
        divisao = num1 / num2
        return divisao
    else:
        return "Operação inválida"

def chamarCalculadora():
    condicao = 0

    while condicao == 0:
        print("Qual operação quer realizar?\n1 - soma; 2 - Subtração; 3 - Multiplicação; 4 - Divisão; 5 - Sair")
        operacao = int(input())
        if operacao == 5:
            condicao = 1
            break
        elif operacao not in (1, 2, 3, 4):
            print("Essa operação não existe")
        else:
            print("Insira o primeiro número: ")
            num1 = int(input())
            print("Insira o segundo número: ")
            num2 = int(input())
            resultado = calculadora(num1, num2, operacao)
            print("O resultado é:", resultado)

chamarCalculadora()
