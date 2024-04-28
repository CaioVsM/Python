VALOR_LIMITE = 500
QUANTIDADE_LIMITE_DIA = 3
saque_quantidade = 0
saldo_atual = 0
extrato = f"""
++++++++++++++++++++++++++++++++
           Extrato


"""

menu_operacao = """
++++++++++++++++++++++++++++++++
           Operações

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

++++++++++++++++++++++++++++++++
==> """

menu_deposito = f"""
++++++++++++++++++++++++++++++++
           Deposito

    Saldo atual: {saldo_atual}

++++++++++++++++++++++++++++++++
Valor: ==> """

menu_saque = f"""
++++++++++++++++++++++++++++++++
           Saque
           
"""

def continuar():
    if input("Realizar outra operação? [s/n] ") == "n":
        exit()
    
while True:
    op = int(input(menu_operacao))
    if op == 1: # Depositar
        while True:
            valor_deposito = float(input(menu_deposito).replace(",", "."))
            if valor_deposito > 1:
                saldo_atual += valor_deposito
                extrato += f"Deposito ___________ R$ {valor_deposito:.2f}\n"
                print("Deposito realizado com sucesso!\n")
                break
            else:
                print("Valor inválido, deposite um valor positivo.\n")
    elif op == 2: # Sacar
        if saque_quantidade < QUANTIDADE_LIMITE_DIA:
            while True:
                menu_saque += f"""
Saldo Atual: _______ R$ {saldo_atual:6.2f}\n
Limite: ____________ R$ {VALOR_LIMITE:6.2f}\n

++++++++++++++++++++++++++++++++
Valor: ==> """
                if saldo_atual > 0:
                    saque = float(input(menu_saque).replace(",", "."))
                    if saque > 1 and saque <= VALOR_LIMITE:
                        saldo_atual -= saque
                        saque_quantidade += 1
                        extrato += f"Saque ______________ R$ {saque:.2f}\n"
                        print("Saque efetuado com sucesso!\n")
                        break
                    else:
                        print("Valor inválido, tente novamente.\n" if saque <= 0 else "Limite de saque ultrapassado, tente outro valor.\n")
                        break
                else:
                    print("Você não possui saldo disponível para saques.\n")
                    break
        else: 
            print("Quantidade de saques diários atingido, tente novamente outro dia.\n")
    elif op == 3: # Extrato
        print(extrato)
        print(f"\nSaldo Atual: ________ R$ {saldo_atual:.2f}\n")
    elif op == 0: # Sair
        break
    else:
        print("Operação invalida, tente novamente.\n")
        continue
    continuar()
