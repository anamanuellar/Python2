class ContasBancarias:
    def __init__(self):
        self._saldo = 0.0           #Atributo privado a classe por convençao
        
    @property
    def saldo(self):                 #getter (Obter o valor do atributo 'privado)
        return self._saldo
    
    #Criando um mtodo Setter (o que atribui)
    #Metodo para adiconar valor ao 
    #saldo existente
    
    @saldo.setter               #Setter(Modifica o atributo "privado")
    def saldo(self, valor):
        if (self._saldo+valor)>=0.0:
            self._saldo += valor
            return True
        else: 
            return False

MinhaCP = ContasBancarias()
print(MinhaCP.saldo)
MinhaCP.saldo = 1000.0
print(MinhaCP.saldo)
MinhaCP.saldo = -250.0
MinhaCP.saldo = -333.0
print(MinhaCP.saldo)
MinhaCP.saldo = -418.0 # Nao saca, continua o saldo anterior
print(MinhaCP.saldo)