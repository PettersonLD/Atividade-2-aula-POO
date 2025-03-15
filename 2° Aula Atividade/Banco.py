#1
class Conta_Bancaria:
    def __init__(self,titular, saldo):
        self.titular = titular
        self.saldo = saldo
        Conta_Bancaria.total_contas += 1
#2
    taxa_de_juros = 0
    total_contas = 0
#3
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("O valor não pode ser zero ou negativo")  
#4
    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                print("Saldo insuficiente")
        else:
            print("Valor inválido")
#5
    def verificar_saldo(self):
        print(f"O saldo atual da conta é de R${self.saldo}")
#6
    @classmethod
    def ajustar_taxa_juros(cls, nova_taxa):
        if nova_taxa > 0:
            cls.taxa_juros = nova_taxa
            print(f"Taxa de juros ajustada para {cls.taxa_juros}%.")
        else:
            print("A taxa de juros deve ser positiva.")
#7
    @classmethod
    def mostrar_total_contas(cls):
        print(f" A quantidade total de contas bancárias é de {cls.total_contas}")
#8
    @staticmethod
    def converter_moeda(valor, taxa_conversao):
            valor_convertido = valor * taxa_conversao
            return valor_convertido
#9
    @staticmethod
    def dias_no_ano():
        return (f"{365} dias")

