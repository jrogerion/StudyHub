from time import sleep

menu = """\n
================ MENU ================
[ 1 ] - Sacar
[ 2 ] - Depositar
[ 3 ] - Extrato
[ 0 ] - Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "0":
        print("Saindo...")
        sleep(3)
        break

    # Operação de saque

    elif opcao == "1":
        valor = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Valor informado inválido.")

    # Operação de depósito
    elif opcao == "2":
        valor = float(input("Valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é inválido.")


    # Operação gerar extrato
    elif opcao == "3":
        print("\n============== EXTRATO ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")

print("## Operação finalizada ##")

