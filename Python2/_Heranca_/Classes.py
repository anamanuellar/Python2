class Fornecedores:
    def __init__(self, nome="", endereco=""):
        self._codigo = 0
        self.nome = nome
        self.endereco = endereco
        
    
    def cadastrar(self):
        self._codigo += 1
    
    def excluir(self):
        pass
    
class Pessoas:
    def __init__(self, nome='', cpf=0, dataNascimento=''):
        self.nome = nome
        self.cpf = cpf
        self.dataNascimento = dataNascimento
    def imprimirNome(self):
        return self.nome.upper()
    
class pessoaFisica(Pessoas):
    pass

class pessoaJuridica(Pessoas):
    def __init__(self, nome='', dataNascimento='', ie=''):
        super().__init__(nome, dataNascimento)
        self.ie = ie

class Veiculo:
    def __init__(self, marca, modelo, velocidadeMax, capacidade, tanque):
        self.marca = marca
        self.modelo = modelo
        self.velocidadeMax = velocidadeMax
        self.velocidadeAtual = 0
        self.capacidade = capacidade
        self.tanque = tanque
        self.ligado = False
            
    def ligar(self):
        if self.ligado:
            print('O veiculo ja esta ligado!')
        else:
            self.ligado = True
            print('O veiculo foi ligado!')
            
    def desligar(self):
        if self.ligado:
            print('O veiculo ja esta ligado!')
        else:
            self.ligado = False
            print('O veiculo foi ligado!')        


# Super classe
class Entidades:
    def __init__(self, atrib1, atrib2, atrib3):
        self.atrib1 = atrib1
        self.atrib2 = atrib2
        self.atrib3 = atrib3
    
    def mostrarDados(self) -> list:
        return {
            1: self.atrib1,
            2: self.atrib2,
            3: self.atrib3,
            }
        
class Filha1(Entidades):
    pass

class Filha2(Entidades):
    pass

objFilha1 = Filha1('Ana', 'Manuella', 'Ribeiro')
print(objFilha1.mostrarDados()[2])
