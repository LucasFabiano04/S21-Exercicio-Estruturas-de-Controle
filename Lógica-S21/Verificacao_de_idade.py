# Programa para verificar a faixa etária de várias pessoas até o usuário decidir parar

while True:  # Laço que continuará até o usuário decidir parar
    idade = int(input("Digite a idade da pessoa (ou digite -1 para parar): "))  # Solicita a idade
    
    if idade == -1:  # Verifica se o usuário quer parar o programa
        print("Programa encerrado.")
        break  # Sai do laço se o usuário digitar -1
    
    # Estrutura de decisão composta para verificar a faixa etária
    if idade < 18:
        print("Menor de idade")  # Se a idade for menor que 18, é menor de idade
    elif 18 <= idade < 60:
        print("Adulto")  # Se a idade for entre 18 e 59, é adulto
    else:
        print("Idoso")  # Se a idade for 60 ou mais, é idoso
