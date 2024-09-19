# O programa irá pedir uma senha ao usuário até que ele acerte

senha_correta = "segura123"  # A senha correta que o usuário precisa inserir

while True:  # Loop que continuará até que o usuário insira a senha correta
    senha = input("Digite a senha: ")  # Solicita a senha ao usuário
    
    if senha == senha_correta:  # Verifica se a senha inserida é igual à senha correta
        print("Acesso permitido")  # Se acertar, exibe mensagem de sucesso
        break  # Interrompe o loop, pois o usuário acertou a senha
    else:
        print("Senha incorreta")  # Caso a senha esteja errada, informa o erro
