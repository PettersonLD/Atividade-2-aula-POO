class Conta_Bancaria:
    def __init__(self, titular, conta):
        self.titular = titular  # Atributo para o nome do titular
        self.conta = conta      # Atributo para o número da conta

# Criando uma instância da Conta_Bancaria
minha_conta = Conta_Bancaria("João Silva", "12345-6")

# Acessando os atributos da instância
# print(f"Titular: {minha_conta.titular}")
# print(f"Número da conta: {minha_conta.conta}")

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
conta1 = Conta_Bancaria("João Silva", "12345-6")
conta2 = Conta_Bancaria("Maria Oliveira", "78910-1")
conta3 = Conta_Bancaria("Carlos Souza", "11223-4")

# Acessando os atributos de classe
# print(f"Taxa de juros: {Conta_Bancaria.taxa_juros}")
# print(f"Total de contas criadas: {Conta_Bancaria.total_contas}")

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
