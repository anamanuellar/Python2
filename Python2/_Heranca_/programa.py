from Classes import *

class Vendedores(Fornecedores):
    def __init__(self, nome, vendas=''):
        super().__init__(nome)
        self.vendas = vendas
    
    def CalcularComissao(self):
        return self.vendas * 0.10
        

class Motocicletas(Veiculos):
    def __init__(self, marca, modelo, ano, posicaoMontada: bool):
        super().__init__(marca, modelo, ano)
        self.posicaoMontada = posicaoMontada

    def naGarantia(self):
        if self.posicaoMontada == self.Garantia:
            return True

        
vendedora1 = Vendedores('José', 500)
print(vendedora1.CalcularComissao())


tipoVeiculo = Motocicletas('Volkswagen', 'Gol', '2005', True)
print(tipoVeiculo.posicaoMontada())