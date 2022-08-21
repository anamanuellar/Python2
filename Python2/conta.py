class Cliente:
				def	__init__(self,	nome,	sobrenome,	cpf):
								self.nome	=	nome
								self.sobrenome	=	sobrenome
								self.cpf	=	cpf

class Contas:
    # Construtor de objetos
    def __init__(self, titular, conta):
        self.titular = titular
        self.conta = conta
        self._saldo = 0
        self._vip = False
        
    #Depositar
    def depositar(self, valor):
        self._saldo += valor
        if self._saldo >= 10000:
            self._vip = True
        self.extrato(valor)
        
    #Sacar
    def sacar(self, valor):
        if valor<= self._saldo:
            self._saldo -= valor
            self.extrato(valor)
            if self._saldo < 10000:
                self._vip = False
            return True
        else:
            return False
    
    #Extrato
    def	extrato(self, valor):
        return[self._saldo, valor]
    