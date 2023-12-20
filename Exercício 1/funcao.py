def calculadora(num1, num2, operacao):
    match operacao:
        case "soma":
            soma = num1 + num2
            return soma
        case "subtracao":
            subtracao = num1 - num2
            return subtracao
        case "multiplicacao":
            multiplicacao = num1 * num2
            return multiplicacao
        case "divisao":
            divisao = num1 / num2
            return divisao
    
print(calculadora(25,5,"multiplicacao"))