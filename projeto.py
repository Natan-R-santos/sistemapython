#Sistema em Python de um simples sistema bancario
print("BEM VINDO AO BANCO SLOWBURN!")
saldo = 0
extrato = []
while True:
    opcao = input("Escolha uma ação:")
    if opcao == "1":
        valor_deposito = float(input("Digite um valor:"))
        if valor_deposito > 0:
        saldo += valor_deposito
        extrato.append(f"Deposito + {valor_deposito:.2}")
        print(f"Deposito feito com sucesso! Seu saldo é: {saldo:.2}")
    elif opcao == "2":
        print(f"Seu saldo é de: {saldo:.2}")
    elif opcao == "3":
        valor_saque = float(input)
        if valor_saque > saldo:
            extrato.append(f"Valor saque: - {valor_saque:.2}")
            print("Saldo Insuficiente!")
            elif valor_saque <= saldo:
                print("Opção Invalida!")
            else:
                saldo -= valor_saque
    elif opcao == "4":
        if not extrato:
            print("Nenhuma Movimentação!")
        else:
            for movimentacao in extrato:
                print(movimentacao)
    elif opcao == "0":
        break
    else:
        print('Opção Invalida!')

