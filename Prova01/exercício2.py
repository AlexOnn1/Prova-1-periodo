#1. Escreva um programa que leia os limites inferior e superior de um intervalo e imprima todos os números pares no intervalo aberto e o seu somatório.
print("=====Exercício 1=====")
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
somatorio=0
for i in lista_numeros:
    
    if i % 2 == 0:
          print(i)
          somatorio = somatorio + i

        

print("Somatório: ", somatorio)   
print("")


#2. Criar um programa que leia 10 números inteiros e imprima o maior e o menor número.  
print("=====Exercício 2=====")         
lista_numeros2 = [14, 21, 3, 5, 123, 154, -5, 2, 40]
maior = 0
menor =0

for i in lista_numeros2:
    
    if i > maior:
        maior = i       
    elif i < menor:
        menor = i
       
print("Maior: ", maior)
print("Menor: ", menor)            
print("")

#3. Escreva um programa que receba várias idades e que calcule e mostre a média das idades. O programa deve finalizar apenas quando for digitada a idade igual a zero.

idade = int(input("Insira sua idade: "))
lista_idade = []

while idade != 0:
    lista_idade.append(idade)
    idade = int(input("Insira sua idade: "))
    
media = sum(lista_idade)/len(lista_idade)     
print("Média da soma das idades: ", media)
print("") 

#4. Escreva um programa que permita registar o nome, a altura e o peso de duas pessoas e apresente o nome da mais pesada e o nome da mais alta.

Marcela = {
    "nome" : "Marcela",
    "altura" : 1.8,
    "peso" : 76
}   

Joana = {
    "nome" : "Joana",
    "altura" : 2,
    "peso" : 45
}

if Marcela["altura"]>Joana["altura"]:
    print(Marcela["nome"], " é a mais alta com", Marcela["altura"], "m")
else:
    print(Joana["nome"], " é a mais alta com", Joana["altura"], "m")
    
if Marcela["peso"]>Joana["peso"]:
    print(Marcela["nome"], " é a mais pesada com", Marcela["peso"], "kg")
else:
    print(Joana["nome"], " é a mais pesada com", Joana["peso"], "kg")    