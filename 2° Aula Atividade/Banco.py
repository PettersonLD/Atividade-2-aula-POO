#1
class Conta_Bancaria: 
    total_contas = 0
    taxa_de_juros = 0
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
        Conta_Bancaria.total_contas += 1
        print(f"Conta criada para {self.titular} com saldo de R${self.saldo}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depositado R${valor}. Novo saldo: R${self.saldo}")
        else:
            print("O valor não pode ser zero ou negativo")  

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Sacado R${valor}. Novo saldo: R${self.saldo}")
            else:
                print("Saldo insuficiente")
        else:
            print("Valor inválido")

    def verificar_saldo(self):
        print(f"O saldo atual da conta é de R${self.saldo}")

    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa > 0:
            cls.taxa_juros = nova_taxa
            print(f"Taxa de juros ajustada para {cls.taxa_juros}%.")
        else:
            print("A taxa de juros deve ser positiva.")

    @classmethod
    def mostrar_total_contas(cls):
        print(f"A quantidade total de contas bancárias é de {cls.total_contas}")

    @staticmethod
    def converter_moeda(valor, taxa_conversao):
        valor_convertido = valor * taxa_conversao
        print(f"Valor convertido: R${valor_convertido}")
        return valor_convertido

    @staticmethod
    def dias_no_ano():
        print("365 dias no ano")
        return "365 dias"

conta1 = Conta_Bancaria("João", 1000)
conta1 = Conta_Bancaria("João", 1000)
conta1 = Conta_Bancaria("João", 1000)
conta1 = Conta_Bancaria("João", 1000)
conta1 = Conta_Bancaria("João", 1000)
#2
print(Conta_Bancaria.total_contas)
# #3
conta1.depositar(500)
# #4
conta1.sacar(200)
conta1.sacar(1500)
# #5
conta1.verificar_saldo()
# #6
Conta_Bancaria.ajustar_taxa_juros(5)
# #7
Conta_Bancaria.mostrar_total_contas()
# #8
Conta_Bancaria.converter_moeda(100, 5.25)
# #9
Conta_Bancaria.dias_no_ano()