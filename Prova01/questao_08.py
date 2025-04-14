# Solicita a string ao usuário
texto = input("Digite a string: ")

# Solicita o caractere a ser buscado
caracter = input("Digite o caractere a ser buscado: ")

# Converte ambos para minúsculas para evitar problemas com maiúsculas/minúsculas
texto = texto.lower()
texto_sem_espacos = texto.replace(" ", "")
caracter = caracter.lower()

if texto_sem_espacos.count(caracter)==0:
    print("O caractere '", caracter, "' não aparece na string.")
else:
    print("O caractere '", caracter, "' aparece ", texto_sem_espacos.count(caracter), " vezes na string.")