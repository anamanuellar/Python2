class Contas:
    # Construtor de objetos
    def __init__(self, titular, conta, vip):
        self.titular = titular
        self.conta = conta
        self.saldo = 0
        self.vip = vip
        
    #Depositar
    def depositar(self, valor):
        self.saldo += valor
        
    #Sacar
    def sacar (self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False
    
    def	extrato(self):
	    print("conta:	{}	\nsaldo:	{}".format(self.conta,	self.saldo))