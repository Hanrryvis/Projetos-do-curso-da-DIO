from abc import ABC,abstractproperty,abstractclassmethod
numero_de_contas = 0

class Cliente:
    
    def __init__(self,endereco,contas):
        self.endereco = endereco
        self.contas = contas

    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):

    def __init__(self,cpf,nome,data_nascimento,endereco,contas):
        super().__init__(endereco,contas)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:

    def __init__(self,numero,cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero,cliente):
        return cls(numero,cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def cliente(self):
        return self._cliente   

    @property
    def historicos(self):
        return self._historico
        
    def sacar(self, valor):
        saldo = self._saldo

        if valor > saldo:
            print("=== Operação falhou, Você não possui saldo sulficiente! === ")

            return False

        elif valor > 0:
            self._saldo -= valor
            print("=== Operação de saque realizada com sucesso! ===") 

            return True

        else:
            print("=== Operação falhou, valor informado é inválido! === ")

            return False

    def depositar(self, valor):
        saldo = self._saldo

        if valor > 0:
            self._saldo += valor
            print("=== Operação de saque realizada com sucesso! ===") 

        else:
            print("=== Operação falhou, valor informado é inválido! === ")

class ContaCorrente(Conta):

    def __init__(self,numero,cliente,limite = 500,limite_saques = 3):
        super().__init__(numero,cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self,valor):

        saques = len([transacao for transacao in self.historicos.transacoes if transacao["tipo"] == Saque.__name__])

        if valor > self._limites:
            print("=== Operação falhou, o valor informado está acima do seu limite! ====")

        elif saques >= self._limite_saques:
            print("=== Operação falhou, você atingiu seu limite de saques hoje! ===")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""
            Agência: {self._agencia}
            Conta: {self._numero}
            Titular: {self._cliente}
"""

class Historico:

    def __init__(self):
        self._transacoes = []


    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self,transacao):
        
            self._transacoes.append({
                    "Tipo":transacao.__class__.__name__,
                    "Valor": transacao.valor,
                    "Data": "04/11/2004"
            })

class Transacao(ABC):


    @property
    @abstractproperty
    def valor(self):
        pass
    
    @abstractclassmethod
    def registrar(self,conta):
        pass

class Saque(Transacao):

    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):
        valido = conta.sacar(self._valor)

        if valido:
            conta.historicos.adicionar_transacao(self)

class Depositar(Transacao):

    def __init__(self,valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self,conta):

        conta.historicos.adicionar_transacao(self)
    

   
def verifica_cpf(cpf):
    
    for cliente in clientes:
        if cpf == cliente.cpf:
            print(f"=== Login realizado com sucesso ===")
            return cliente
    print("@@@ úsuario não encontrado @@@")
    return False

def deposito(valor,cliente):

    cliente.depositar(valor)
    Depositar(valor).registrar(cliente)

def saque(valor,cliente):


    cliente.sacar(valor)
    Saque(valor).registrar(cliente)

def adicionar_usuario(clientes):

    nome = input("Digite seu nome:")
    data = input("Digite a sua data de nascimento:")
    cpf = input("Digite seu CPF (somente números):")
    endereco = input("Digite seu endereço:")

    usuario = PessoaFisica(endereco = endereco,cpf = cpf,data_nascimento = data,nome = nome,contas = [])
    clientes.append(usuario)

    return clientes

def criar_conta(contas,cliente):

    global numero_de_contas 
    numero_de_contas += 1

    conta = ContaCorrente.nova_conta(numero_de_contas,cliente)

    if conta:
        print("=== Conta criada com sucesso ===")

    contas.append(conta)
  

    return contas,conta

def Extrato(cliente):

    extrato = cliente.historicos.transacoes

    for movimentacao in extrato:
        print(f"""
            "Ação: " {movimentacao["Tipo"]}
            "Valor: " {movimentacao["Valor"]} "\n"
""")

def Exibir_usuarios(clientes):
    for cliente in clientes:

        print(f'''
=======================================================
              
            Nome: {cliente.nome}
            Endereço: {cliente.endereco}
            Data de Nascimento: {cliente.data_nascimento}

========================================================
''')

def Listar_contas(contas):
    for conta in contas:

        print(f'''
==========================================================
              
            Nome: {conta.cliente.nome}
            Número de conta: {conta.numero}
            Agência: {conta._agencia}

==========================================================
''')

menu1 ='''
============================================
               MENU

            Add usúario [A]
            Login usúario [L]
            Fechar [F]

=============================================
''' 


menu2 = f'''============================================
                MENU 
      
            Criar conta [C]
            Depósito [D]
            Saque [S]
            Visualizar Extrato [V]
            Exibir usuarios [E]
            Listar contas [L]
            Fechar [F]

=============================================
''' 
clientes = []
contas =[]

while True:

    opcao = input(menu1)

    if opcao == "A":
        clientes = adicionar_usuario(clientes)
        print("=== perfil adicionado com sucesso ===")

    elif opcao == "L":
        logado_cliente = verifica_cpf(input("digite seu cpf: "))

        if logado_cliente:
            while True:
            
                print(f"\n Cliente: {logado_cliente.nome}")
                opcao = (input(menu2))
        
            
                if opcao == 'D':

                    if logado_conta:
                        valor = int(input("Digite o valor que deseja depositar: "))
                        deposito(valor,logado_conta)
                    else:
                        print("@@@@ Crie uma conta para realizar transações @@@@")

                elif opcao == 'S':

                    if logado_conta:
                        valor = int(input("Digite o valor que deseja sacar: "))
                        saque(valor,logado_conta)
                    else:
                        print("@@@@ Crie uma conta para realizar transações @@@@")

                elif opcao == "V":
                    if logado_conta:
                        Extrato(logado_conta)
                    else:
                        print("@@@@ Crie uma conta para visualizar suas transações @@@@")
        
                elif opcao == "C":

                    contas,logado_conta = criar_conta(contas,logado_cliente)


                elif opcao == 'E':
                
                    Exibir_usuarios(clientes)

                elif opcao == "L":
                
                    Listar_contas(contas)

                elif opcao == 'S':
                    break

                else:
                        print("digite uma opção valida")

        else:
            print("cliente não encontrado")

    elif opcao == 'S':
        break    

    else:     
        print("digite uma opção valida")
                    