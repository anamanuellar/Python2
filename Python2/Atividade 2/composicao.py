#Associacao entre classes:
class Salarios:
    def __init__(self, qtHoras, valorHora, adicional=0):
        self.qtHoras = qtHoras
        self.valorHora = valorHora
        self.adicional = adicional
        
    def calcularSalarios(self):
        return (self.qtHoras*self.valorHora + self.adicional)
    
#Classe Todo:
class Funcionarios:
    def __init__(self, nome, cpf, endereço, qtHoras, valorHora, adicional):
        self.nome = nome
        self.cpf = cpf
        self.endereço= endereço
        self.salario = Salarios(qtHoras, valorHora, adicional)
        
vendedor = Funcionarios('Marta Silva', '123.456.678-90', 'Ruas das Flores, 007', 15, 100, 0.1)
print(vendedor.nome, ' = R$', vendedor.salario.calcularSalarios())