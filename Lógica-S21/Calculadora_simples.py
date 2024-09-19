# Calculadora simples que realiza operações de adição, subtração, multiplicação e divisão

def calculadora():  # Função que contém a lógica da calculadora
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite o número da operação desejada (1/2/3/4): ")  # Usuário escolhe a operação

    if operacao not in ['1', '2', '3', '4']:  # Verifica se a operação é válida
        print("Operação inválida. Por favor, escolha uma opção entre 1 e 4.")
        return  # Sai da função se a operação for inválida

    # Solicita os dois números para realizar a operação
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Estrutura de decisão composta para realizar a operação escolhida
    if operacao == '1':
        resultado = num1 + num2  # Adição
        print(f"{num1} + {num2} = {resultado}")
    elif operacao == '2':
        resultado = num1 - num2  # Subtração
        print(f"{num1} - {num2} = {resultado}")
    elif operacao == '3':
        resultado = num1 * num2  # Multiplicação
        print(f"{num1} * {num2} = {resultado}")
    elif operacao == '4':
        if num2 != 0:  # Verifica se o divisor não é zero para evitar erro de divisão
            resultado = num1 / num2  # Divisão
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")  # Mensagem de erro para divisão por zero

# Executa a função
calculadora()
