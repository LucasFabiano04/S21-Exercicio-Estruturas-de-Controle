# Programa para calcular a média de vários alunos e classificá-los como Aprovado, Recuperação ou Reprovado

while True:  # Laço que continua até o usuário decidir parar
    # Solicita as notas do aluno
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))

    # Calcula a média
    media = (nota1 + nota2) / 2
    
    # Estrutura de decisão composta para classificação
    if media >= 7:
        print(f"Média {media:.2f} - Aprovado")  # Aprovado se a média for 7 ou mais
    elif 5 <= media < 7:
        print(f"Média {media:.2f} - Recuperação")  # Recuperação se a média for entre 5 e 6.9
    else:
        print(f"Média {media:.2f} - Reprovado")  # Reprovado se a média for abaixo de 5

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja inserir as notas de outro aluno? (s/n): ").lower()
    if continuar != 's':  # Se o usuário digitar algo diferente de 's', o laço termina
        print("Encerrando o programa.")
        break
