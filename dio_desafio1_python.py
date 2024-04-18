menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
saldo = 0
limite = float(500)
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
while True:
    opcao = input(menu)
    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito:R$ "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}\n"
        else:
            print(" O valor informado é inválido.")
    elif opcao == "s":
         if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Informe o valor do saque: R$ "))
            if valor_saque > 0:
                if valor_saque <= limite :
                   if valor_saque <= saldo:
                      saldo -= valor_saque
                      extrato += f"Saque: R$ {valor_saque:.2f}\n"
                      numero_saques += 1
                   else:
                      print(f"Você não tem saldo suficiente ")    
                else:
                    print(f"O limite de saque é de {limite:.2f}")
            else:
                print("Você deve informar um valor de saque válido!")
         else: 
                print(f"Você não pode efetuar o saque pois excedeu  o limite diário {LIMITE_SAQUES}") 
            
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")