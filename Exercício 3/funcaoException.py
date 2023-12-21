def nomeIdade ():
    getOut = False

    nome = str(input("Digite seu nome: "))
    
    while(getOut == False):
        try:
            anoNascimento = int(input("Digite ano de nascimento: ")) 

            if(1922 <= anoNascimento <= 2021):
                idade = 2022 - anoNascimento
                print(f'Olá, {nome}, você nasceu em {anoNascimento} e em 2022 tem {idade} anos')
                getOut = True
            elif(anoNascimento > 2021):
                print("Ano precisa ser menor que 2022")
            elif(anoNascimento < 1922):
                print("Ano precisa ser maior que 1922")
        except:
            print("Ano inválido! Verifique se digitou corretamente com número inteiros")

nomeIdade()