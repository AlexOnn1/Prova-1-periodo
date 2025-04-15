while True:
    while True:  # Loop para validar a entrada
        try:
            numero = int(input("Insira um número inteiro: "))
            break  # Sai do loop se a entrada for válida
        except ValueError:
            print("Entrada inválida! Por favor, insira um número inteiro.")

    # Verifica se o número é primo
    if numero >= 1:
        for i in range(2, int(numero ** 0.5) + 1):
            if numero % i == 0:
                print(numero, " não é um número primo.")
                break
        else:
            print(numero, " é um número primo.")
    else:
        print(numero, " não é um número primo.")

    # Pergunta ao usuário se deseja continuar
    continuar = input("Deseja verificar outro número? (sim/não): ").strip().lower()
    if continuar == "não" or continuar == "nao":
        print("Encerrando o programa. Até mais!")
        break
