# Programa para inserir o nome e a nota de 5 alunos, calcular a média da turma e classificar cada um

alunos = []  # Lista para armazenar os nomes dos alunos
notas = []   # Lista para armazenar as notas dos alunos
soma_notas = 0  # Variável para somar as notas e calcular a média

# Estrutura de repetição para solicitar os dados de 5 alunos
for i in range(5):
    nome = input(f"Digite o nome do {i+1}º aluno: ")  # Solicita o nome do aluno
    nota = float(input(f"Digite a nota do {i+1}º aluno: "))  # Solicita a nota do aluno
    
    alunos.append(nome)  # Adiciona o nome à lista de alunos
    notas.append(nota)  # Adiciona a nota à lista de notas
    soma_notas += nota  # Soma a nota à variável soma_notas

# Calcula a média da turma
media_turma = soma_notas / 5

print(f"\nMédia da turma: {media_turma:.2f}\n")

# Estrutura de repetição para classificar cada aluno
for i in range(5):
    # Estrutura de decisão composta para classificar o aluno
    if notas[i] >= 7:
        print(f"{alunos[i]} - Aprovado com nota {notas[i]:.2f}")
    else:
        print(f"{alunos[i]} - Reprovado com nota {notas[i]:.2f}")
