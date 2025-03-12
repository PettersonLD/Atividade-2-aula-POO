# Atividade 1
class Conta_Bancaria:
    def __init__(self, titular, conta):
        self.titular = titular  # Atributo para o nome do titular
        self.conta = conta      # Atributo para o número da conta

# Criando uma instância da Conta_Bancaria
#minha_conta = Conta_Bancaria("João Silva", "12345-6")

# Acessando os atributos da instância
# print(f"Titular: {minha_conta.titular}")
# print(f"Número da conta: {minha_conta.conta}")




# Atividade 2
class Conta_Bancaria:
    # Atributos de classe
    taxa_juros = 0.05  # Definindo uma taxa de juros padrão de 5%
    total_contas = 0    # Inicia o contador de contas em 0
    
    def __init__(self, titular, conta):
        # Atributos de instância
        self.titular = titular
        self.conta = conta
        
        # Incrementa o contador total de contas a cada nova instância
        Conta_Bancaria.total_contas += 1


# Criando algumas instâncias da Conta_Bancaria
#conta1 = Conta_Bancaria("João Silva", "12345-6")
#conta2 = Conta_Bancaria("Maria Oliveira", "78910-1")
#conta3 = Conta_Bancaria("Carlos Souza", "11223-4")

#Acessando os atributos de classe
#print(f"Taxa de juros: {Conta_Bancaria.taxa_juros}")
#print(f"Total de contas criadas: {Conta_Bancaria.total_contas}")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Atividade 3
class Conta_Bancaria:
    # Atributos de classe
    taxa_juros = 0.05  # Definindo uma taxa de juros padrão de 5%
    total_contas = 0    # Inicia o contador de contas em 0
    
    def __init__(self, titular, conta):
        # Atributos de instância
        self.titular = titular
        self.conta = conta
        self.saldo = 0  # Inicia o saldo da conta como 0
        
        # Incrementa o contador total de contas a cada nova instância
        Conta_Bancaria.total_contas += 1
    
    def depositar(self, valor):
        # Verifica se o valor é positivo
        if valor > 0:
            self.saldo += valor  # Adiciona o valor ao saldo da conta
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Erro: O valor do depósito não pode ser zero ou negativo.")

# Criando uma instância da Conta_Bancaria
# conta1 = Conta_Bancaria("João Silva", "12345-6")

# Realizando depósitos
# conta1.depositar(500)  # Depósito válido
# conta1.depositar(-50)  # Tentativa de depósito negativo
# conta1.depositar(200)  # Depósito válido

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Atividade 4
class Conta_Bancaria:

    total_contas = 0

    def __init__(self, titular, conta,):
        self.titular = titular
        self.conta = conta
        self.saldo = 300

        Conta_Bancaria.total_contas += 1

    def sacar(self, valor):
        
            if valor <= self.saldo:
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Erro: Saldo insuficiente.")

# Criando uma instância da Conta_Bancaria
#conta1 = Conta_Bancaria("João Silva", "12345-6")

# Realizando saques
#conta1.sacar(200)  # Saque válido
#conta1.sacar(500)  # Tentativa de saque com saldo insuficiente
#conta1.sacar(100)  # Saque válido

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Atividade 5
class Conta_Bancaria:

    total_contas = 0

    def __init__(self, titular, conta):
        self.titular = titular
        self.conta = conta
        self.saldo = 300

        Conta_Bancaria.total_contas += 1

    def verificar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

#Visualizando o saldo da conta
#conta1 = Conta_Bancaria("João Silva", "12345-6")

#conta1.verificar_saldo()  # Saldo atual: R$300.00

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Atividade 6
class Conta_Bancaria:
    # Atributos de classe
    taxa_juros = 0.05  # Definindo uma taxa de juros padrão de 5%
    total_contas = 0    # Inicia o contador de contas em 0

    def __init__(self, titular, conta):
        # Atributos de instância
        self.titular = titular
        self.conta = conta
        self.saldo = 300

        # Incrementa o contador total de contas a cada nova instância
        Conta_Bancaria.total_contas += 1

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa >= 0:
            cls.taxa_juros = nova_taxa
            print(f"Taxa de juros ajustada para: {cls.taxa_juros * 100}%")
        else:
            print("Erro: A taxa de juros deve ser positiva.")


#---------------------------------------------------------------------------------------------------------------------------

#Atividade 7
class Conta_Bancaria:
    # Atributos de classe
    taxa_juros = 0.05  # Definindo uma taxa de juros padrão de 5%
    total_contas = 0    # Inicia o contador de contas em 0

    def __init__(self, titular, conta):
        # Atributos de instância
        self.titular = titular
        self.conta = conta
        self.saldo = 300

        # Incrementa o contador total de contas a cada nova instância
        Conta_Bancaria.total_contas += 1

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa >= 0:
            cls.taxa_juros = nova_taxa
            print(f"Taxa de juros ajustada para: {cls.taxa_juros * 100}%")
        else:
            print("Erro: A taxa de juros deve ser positiva.")

    @classmethod
    def mostrar_total_contas(cls):
        print(f"Total de contas bancárias criadas: {cls.total_contas}")

# Testando a funcionalidade
#conta1 = Conta_Bancaria("João Silva", "12345-6")
#conta2 = Conta_Bancaria("Maria Oliveira", "78910-1")

#Conta_Bancaria.mostrar_total_contas()  # Deve exibir: Total de contas bancárias criadas: 2

#---------------------------------------------------------------------------------------------------------------------------
#Atividade 8

class Conta_Bancaria:

    @staticmethod
    def converter_moeda(valor, taxa_conversao):
        return valor * taxa_conversao

# Testando o método estático
#valor_convertido = Conta_Bancaria.converter_moeda(100, 5.25)
#print(f"Valor convertido: R${valor_convertido:.2f}")  # Deve exibir: Valor convertido: R$525.00

#---------------------------------------------------------------------------------------------------------------------------
#Atividade 9

class Conta_Bancaria:

    @staticmethod
    def dias_no_ano():
        return 365

# Testando o método estático
dias = Conta_Bancaria.dias_no_ano()
print(f"Número de dias no ano: {dias}")  # Deve exibir: Número de dias no ano: 365
