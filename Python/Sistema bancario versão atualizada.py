numero_de_contas = 0

def deposito(saldo,extrato):

    aux = float(input("Insira o valor que você deseja depositar:"))
    saldo += aux
    extrato += f"\nDepósito de R${aux}"

    return saldo,extrato

def saque(saldo,extrato,limite_saque,saque_max):

    if limite_saque == 0:
        aux2 = input("você já fez 3 saques hoje! Não é possível realizar esta ação")
    else:        
        while True:
            aux = float(input("Insira o valor de até R$500 que você deseja sacar:"))

            if aux > saldo:
                print("Seu saldo é insulficiente, insira um valor válido")
                
            elif aux > saque_max or aux < 0:
                print("Seu limite de saque é de até R$500!, insira um valor válido")
            else:
                limite_saque -= 1
                saldo -= aux
                extrato += f"\nSaque de R${aux}"
                break


    return saldo,extrato,limite_saque -1 

def Extrato(extrato,saldo):

    print(f"\n***********Extrato***********")
    print("você não possui movimentações" if not extrato else extrato)
    print(f"\n Saldo = R$ {saldo}")
    print("*****************************")
    aux = input("Dê enter para voltar ao menu")


    return 

def adicionar_usuario(usuarios):

    nome = input("digite seu nome:")
    data = input("digite a sua data de nascimento:")
    print("digite seu CPF (somente números):")

    while True:
        cpf = input("")
        if "-" in cpf or " " in cpf or "." in cpf: print("formato invalido, digite novamente:")
        elif cpf in usuarios.values() : print("Um úsuario com este cpf já existe, digite outro cpf:")
        else: break

    endereco = input("digite seu endereço:")

    usuarios[cpf] = {"Nome": nome,"Data de nascimento": data, "Endereço" : endereco}

    return usuarios

def criar_conta(contas,usuarios):

    global numero_de_contas 
    numero_de_contas += 1

    login_cpf = input("Qual Digite seu CPF para criação da conta: ")
    

    while True:
    
        verifica = usuarios.get(login_cpf,{})

        if verifica:

            contas[numero_de_contas] = {"Banco" : "0001", "cpf" : login_cpf}
            break 

        else:

            login_cpf =input("cpf não encontrado, digite novamente\n")

    return contas


menu ='''

******************************************
               MENU
      
            1.Depósito 
            2.Saque 
            3.Extrato 
            4.Add usúario 
            5.Criar conta 
            6.Listar usuarios 
            7.Listar contas
            8.Fechar 

obs: Para acessar a opção digite seu número
*******************************************
''' 


saldo = 0
extrato = ""
limite_saque = 3
saque_max = 500
usuarios = {}
contas = {}

while True:

    opcao = int(input(menu))
    
    
    if opcao == 1:
        
        saldo,extrato = deposito(saldo,extrato)

    elif opcao == 2:
        
        saldo,extrato,limite_saque = saque(saldo,extrato,limite_saque,saque_max)

    elif opcao == 3:
       
        Extrato(extrato,saldo)

  
    elif opcao == 4:

        usuarios = adicionar_usuario(usuarios)
  
  
    elif opcao == 5:

        contas = criar_conta(contas,usuarios)


    elif opcao == 6:
        
        for cpf, info in usuarios.items():
            print(f"\nUsuario: {info['Nome']}")
            print(f"CPF: {cpf}")
            print(f"Data de Nasc.: {info['Data de nascimento']}")
            print(f"Endereço: {info['Endereço']}")
        
        input("Pressione enter para voltar ao menu")

    elif opcao == 7:
        
        for conta, info in contas.items():
            print(f"\nConta Número: {conta}")
            print(f"Banco: {info['Banco']}")
            print(f"CPF: {info['cpf']}")

        input("\nPressione enter para voltar ao menu")


    elif opcao == 8:
        break

    else:
        
        print("digite uma opção valida")

            


                