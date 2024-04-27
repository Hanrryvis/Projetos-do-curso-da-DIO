
menu ='''

*********************************
            MENU
      
        1.Depósito (D)
        2.Saque (S) (3)
        3.Extrato (E)
        4.Fechar (F)

*********************************
''' 


saldo = 0
extrato = ""
limite_saque = 3
saque_max = 500


while True:

    opcao = input(menu)
    
    
    if opcao == "D" or opcao == "d":
        
        aux = float(input("Insira o valor que você deseja depositar:"))
        saldo += aux
        extrato += f"\nDepósito de R${aux}"

    elif opcao == "S" or opcao == "s":
        if limite_saque == 0:
                aux2 = input("você já fez 3 saques hoje! Não é possível realizar esta ação")
        else:        
            while True:
                aux = float(input("Insira o valor de até R$500 que você deseja sacar:"))

                if aux > saldo:
                    print("Seu saldo é insulficiente, insira um valor válido")
                
                elif aux > 500 or aux < 0:
                    print("Seu limite de saque é de até R$500!, insira um valor válido")

                else:
                    limite_saque -= 1
                    saldo -= aux
                    extrato += f"\nSaque de R${aux}"
                    break


    elif opcao == "E" or opcao == "e":
        print(f"\n***********Extrato***********")
        print("você não possui movimentações" if not extrato else extrato)
        print(f"\n Saldo = R$ {saldo}")
        print("*****************************")
        aux = input("Dê enter para voltar ao menu")

    else:
        break

            


                