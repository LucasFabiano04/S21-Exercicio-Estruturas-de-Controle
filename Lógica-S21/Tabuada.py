# Programa para imprimir a tabuada de um número

# Solicita um número ao usuário
numero = int(input("Digite um número maior que 0 para ver sua tabuada: "))

# Estrutura de seleção para verificar se o número é válido
if numero > 0:
    print(f"\nTabuada do {numero}:")
    # Estrutura de repetição para calcular e imprimir a tabuada de 1 a 10
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número inválido. Por favor, insira um número maior que 0.")
