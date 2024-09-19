# Programa para calcular o fatorial de um número inteiro positivo

while True:  # Laço para manter o programa rodando até o usuário inserir um número válido
    numero = int(input("Digite um número inteiro positivo: "))  # Solicita um número inteiro
    
    if numero < 0:  # Verifica se o número é negativo
        print("Por favor, insira um número positivo.")
    else:
        fatorial = 1  # Inicializa o valor do fatorial como 1
        for i in range(1, numero + 1):  # Laço para calcular o fatorial
            fatorial *= i  # Multiplica o valor atual pelo índice do laço
        print(f"O fatorial de {numero} é {fatorial}")  # Exibe o resultado
        break  # Interrompe o laço após calcular o fatorial
