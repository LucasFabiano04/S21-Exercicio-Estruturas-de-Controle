# Programa que imprime todos os números pares e ímpares até o número inserido

# Solicita um número ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Laço de repetição para iterar de 0 até o número inserido
for i in range(1, numero + 1):  # Começa em 1 e vai até o número inserido
    # Estrutura de seleção para verificar se o número é par ou ímpar
    if i % 2 == 0:
        print(f"{i} é par")  # Se o número for divisível por 2, é par
    else:
        print(f"{i} é ímpar")  # Caso contrário, é ímpar
