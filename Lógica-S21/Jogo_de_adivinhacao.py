import random  # Importa a biblioteca para gerar um número aleatório

# O computador escolhe um número aleatório entre 1 e 50
numero_secreto = random.randint(1, 50)  

tentativas = 5  # Define o número máximo de tentativas

print("Tente adivinhar o número entre 1 e 50. Você tem 5 tentativas.")

for tentativa in range(1, tentativas + 1):  # Laço para permitir até 5 tentativas
    palpite = int(input(f"Tentativa {tentativa}: "))  # Solicita o palpite do usuário
    
    if palpite == numero_secreto:  # Verifica se o palpite está correto
        print("Parabéns! Você adivinhou o número!")
        break  # Sai do laço se o usuário acertar
    elif palpite < numero_secreto:  # Se o palpite for menor que o número secreto
        print("O número é maior.")
    else:  # Se o palpite for maior que o número secreto
        print("O número é menor.")
    
    if tentativa == tentativas:  # Se o usuário usar todas as tentativas
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")
