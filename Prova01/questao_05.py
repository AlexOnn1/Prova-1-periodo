# Solicita o número de notas
n = int(input("Quantas notas deseja informar? "))

# Lista para armazenar as notas
notas = []

# Lê as notas
for i in range(n):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / n

# Calcula os limites de 10% acima e abaixo da média
limite_acima = media * 1.10  # 10% acima da média
limite_abaixo = media * 0.90  # 10% abaixo da média

# Contadores para as notas acima e abaixo dos limites
acima = 0
abaixo = 0

# Verifica cada nota
for nota in notas:
    if nota > limite_acima:
        acima += 1
    elif nota < limite_abaixo:
        abaixo += 1

# Exibe os resultados
print("Média da turma: ", media:.2f)
print("Notas mais de 10% acima da média: ", acima)
print("Notas menos de 10% abaixo da média: ", abaixo)
