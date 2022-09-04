import datetime


class Cliente:
				def __init__(self,	nome,	sobrenome,	cpf):
								self.nome = nome
								self.sobrenome = sobrenome
								self.cpf = cpf


class Conta:
    # Construtor de objetos
    def __init__(self, numero, cliente, saldo, limite=10000.0):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    # Depositar
    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("depósito	de	{}".format(valor))

    # Sacar
    def saca(self, valor):
    	if(self.saldo < valor):
         return False
        else:
         self.saldo -= valor
         self.historico.transacoes.append("saque	de	{}".format(valor))

    # Extrato
    def extrato(self):
        print("numero:	{}	\nsaldo:	{}".format(self.numero,	self.saldo))
        self.historico.transacoes.append("tirou	extrato	- saldo de {}".format(self.saldo))

    # Transfere
    def transfere(self,	destino,valor):
        retirou = self.saca(valor)
        if (retirou == False):
         return False
        else:
         destino.deposita(valor)
         self.historico.transacoes.append("transferencia	de	{}	para	conta	{}".format(valor,	destino.numero))
         return	True

class Historico():
    def __init__(self):
        self.data_abertura= datetime.datetime.today()
        self.transacoes	= []
    def imprime(self):
	    for t in self.transacoes:
	     print("-",	t)
   

conta = Conta('123-4','João',	120.0,	1000.0)
print(conta.numero, conta.cliente, conta.saldo, conta.limite)
