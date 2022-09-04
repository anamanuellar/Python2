class Pessoas: #Classe Mae ou Super Classe ou Classe Base
    def __init__(self, matricula, nome, dataNasc='') -> None:
        self.matricula= matricula
        self.nome= nome
        self.dataNasc= dataNasc
        
class Professores:
    def __init__(self, matricula, nome, endereco, dataNasc) -> None:
        super().__init__(matricula, nome, dataNasc)
        self._ativo = True
        self.endereco = endereco
        self._dataDemissao = ''
    def prof1():
        return ('Dentro de Prof1')

class Estudantes(Pessoas, Professores):
    def __init__(self, matricula, nome, endereco, dataNasc='') -> None:
        super().__init__(matricula, nome, dataNasc, endereco)
    def AssistirAulas(self):
        pass
    def ParticiparSalaAula(self):
        pass 
    
class Disciplinas:
    def __init__(self, codigo, nomenclatura, horaAula, descricao='') -> None:
        self.codigo = codigo
        self.nomenclatura = nomenclatura
        self.descricao = descricao
        self.horaAula = horaAula
    
class Salas:
    def __init__(self, codigo, sala, qtAlunos):
        self.codigo = codigo
        self.sala = sala
        self.qtAlunos = qtAlunos
        
    