# Leia os valores de entrada
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Certifique-se de que x seja o menor e y o maior
if x > y:
    x, y = y, x

# Itere pelos valores entre x e y (exclusivo)
for num in range(x + 1, y):
    # Verifique se o resto da divisão por 5 é 2 ou 3
    if num % 5 == 2 or num % 5 == 3:
        print(num)