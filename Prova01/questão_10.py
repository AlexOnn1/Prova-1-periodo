# Programa para ler n números inteiros e exibi-los em diferentes ordens

# Lê a quantidade de números que o usuário deseja inserir
n = int(input("Quantos números você deseja inserir? "))

# Lista para armazenar os números
numeros = []

# Lê os números do usuário
for _ in range(n):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

# a) Exibe os números na ordem inversa
print("Números na ordem inversa:")
print(numeros[::-1])

# b) Exibe os números em ordem decrescente
print("Números em ordem decrescente:")
print(sorted(numeros, reverse=True))