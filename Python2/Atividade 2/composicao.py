#Associacao entre classes:
from xmlrpc.client import boolean


class Salarios:
    def __init__(self, qtHoras, valorHora, adicional=0):
        self.qtHoras = qtHoras
        self.valorHora = valorHora
        self.adicional = adicional
        
    def calcularSalarios(self):
        return (self.qtHoras*self.valorHora + self.adicional)
    
#Classe Todo:
class Funcionarios:
    def __init__(self, nome, cpf, endereco, qtHoras, valorHora, adicional, nomeDep=0, qtFuncionarios=0):
        self.nome = nome
        self.cpf = cpf
        self.endereço= endereco
        self.salario = Salarios(qtHoras, valorHora, adicional)
        self.departamento = Departamentos(nomeDep, qtFuncionarios)
   
    def imprimirDep(self):
        return(self.departamento)
        
class Departamentos:
    def __init__(self, nomeDep, qtFuncionarios, adm=False):
        self.nomeDep = nomeDep
        self.qtFuncionarios = qtFuncionarios
        self.adm = adm
        
 
        
vendedor = Funcionarios('Marta Silva', '123.456.678-90', 'Ruas das Flores, 007', 15, 100, 0.1, 'Compras', 32)
print(vendedor.nome, ' = R$', vendedor.salario.calcularSalarios(), 'Departamento: ', vendedor.imprimirDep)
funcionario = Departamentos('Compras', 32)
print('Departamento: ', funcionario.nomeDep, ' Quantidade de funcionarios: ', funcionario.qtFuncionarios)
