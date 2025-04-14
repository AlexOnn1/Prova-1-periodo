idade = int(input("Por favor informe sua idade:"))

if idade < 0:
    print("Precisa nascer.")
elif 0<= idade <=5:
    print("Muito novo para as categorias")

elif 5<= idade <=7:
    print("Infantil")


elif 8<= idade <=10:
    print("Iniciado")


elif 11<= idade <=13:
    print("Juvenil")

elif 14<= idade <=17:
    print("Junior")   
else:
    print("Sênior")     
print("")
#========================================================================

#exercicio 2

valor_compra = float(input("Informe o valor de compra do produto: R$ "))


if valor_compra < 10.00:
    lucro = 0.70  
elif 10.00 <= valor_compra < 30.00:
    lucro = 0.50  
elif 30.00 <= valor_compra < 50.00:
    lucro = 0.40  
else:
    lucro = 0.30 

# Calcula o valor de venda
valor_venda = valor_compra * (1 + lucro)

# Exibe o resultado
print(f"Valor de compra: R$ {valor_compra:.2f}")
print(f"Percentual de lucro aplicado: {lucro * 100:.0f}%")
print(f"Valor de venda: R$ {valor_venda:.2f}")
#========================================================================

#exercicio 3
assiduidade = 80
nota = 14

if assiduidade < 75:
    print("Assiduidade abaixo do mínimo. Reprovado.")
elif 75<= assiduidade <=100 and nota < 5:
    print("Nota abaixo do mínimo. Reprovado.")
elif 75<= assiduidade <=100 and 5<= nota<=9.5:
    print("Nota entre 5 e 9.5. Necessita realizar o exame para ser aprovado.")
elif 75<= assiduidade <=100 and 10<=nota<=20:
    print("Aprovado.")    
else:
    print("Dados inválidos.")    
