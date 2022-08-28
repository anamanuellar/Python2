class Cinema:
    def __init__(self):
        self._idade = 0           #Atributo privado a classe por convençao
        
    @property
    def idade(self):                 #getter (Obter o valor do atributo 'privado)
        return self._idade
    
    #Criando um mtodo Setter (o que atribui)
    #Metodo para adiconar valor ao 
    #idade existente
    
    @idade.setter               #Setter(Modifica o atributo "privado")
    def idade(self, valor):
        if valor >=18:
            self._idade = valor         
        else: 
            print('Entrada proibida')
            
        


FaixaEtaria = Cinema()
print(FaixaEtaria.idade)
FaixaEtaria.idade = 15
print(FaixaEtaria.idade)
FaixaEtaria.idade = 27
print(FaixaEtaria.idade)
FaixaEtaria.idade = 9
print(FaixaEtaria.idade)
FaixaEtaria.idade = 18
print(FaixaEtaria.idade)