
while True:
    nome = input("Digite o nome do convidado: ")[:120]  # Limita a 120 caracteres
    if nome.lower() == "sair":  # Converte a entrada para minúsculas antes de comparar
        break
    print("Seja muito bem-vindo ", nome)