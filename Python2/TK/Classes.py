from mailbox import NotEmptyError


class Fornecedores:
    def __init__(self, nome="", endereco=""):
        self._codigo 
        self.nome = nome
        self.endereco = endereco
    
    def cadastrar():
        pass
    
    def excluir():
        pass
    

class Veiculos:
    def __init__(self, marca, modelo, velMaxima, potencia, tanque) -> None:
        self.marca = marca
        self.modelo =   modelo
        self.potencia = potencia
        self._velAtual = 0
        self.velMaxima = velMaxima
        self.tanque = tanque
        self._ligado = False    
    def ligarDesligar(self):
        if (self._velAtual==0) and (not self._ligado):
            self._ligado = True
        elif (self._velAtual==0) and (self._ligado):
            self._ligado = False
        return self._ligado()
    def acelerarEm(self, valor):
        if (self._velAtual+valor<=self.velMaxima) and (self._ligado):
            self._velAtual += valor
        elif (self._velAtual+valor>self.velMaxima) and (self._ligado):
            self._velAtual = self.velMaxima
        return self._velAtual 
    def frearEm(self, valor):
        if (self._velAtual-valor>=0):
            self._velAtual -= valor
        return self._velAtual 
