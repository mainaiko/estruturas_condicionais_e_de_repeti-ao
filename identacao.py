def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print(f"Valor sacado: {valor}")
        print("Obrigado por ser nosso cliente.")
        print ("Tenha um bom dia")
    else:
        print("Saldo insuficiente")

sacar(400)