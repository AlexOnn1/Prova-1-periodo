numero = int(input("Insira um número: "))
lista_numero = [numero]  # Adiciona o primeiro número diretamente à lista

for i in range(2):  # Loop para adicionar mais dois números
    numero = int(input("Insira um número: "))
    lista_numero.append(numero)
    
print("Lista: ", lista_numero)    
lista_numero.sort()
print("Números em ordem crescente: ", lista_numero)