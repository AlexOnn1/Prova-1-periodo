# Solicita a string ao usuário
texto = input("Digite a string: ")[:100]

# Solicita os caracteres para substituição
caracter1 = input("Digite o primeiro caractere (a ser substituído): ")
caracter2 = input("Digite o segundo caractere (substituto): ")

# Substitui todas as ocorrências do primeiro caractere pelo segundo
texto_modificado = texto.replace(caracter1, caracter2)

# Exibe o resultado
print("String resultante: ", texto_modificado)