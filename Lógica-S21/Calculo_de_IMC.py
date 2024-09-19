# Programa para calcular o Índice de Massa Corporal (IMC) e classificar o resultado

# Solicita o peso e a altura da pessoa
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o valor do IMC
print(f"Seu IMC é: {imc:.2f}")

# Estrutura de decisão composta para classificar o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso normal")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso")
else:
    print("Classificação: Obesidade")
