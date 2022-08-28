class NotaFiscal:
    tamanhoCodigo = 8
    def __init__(self):
        self._codigo = ''
    @property
    def codigo(self):
        return self._codigo 
    
    @codigo.setter              
    def codigo(self, texto):
        if len(texto) == NotaFiscal.tamanhoCodigo and texto [0:2] =='NF':
            self._codigo = texto
        else: 
            print('NF invalida')
        
TalaoNF = NotaFiscal()
print(TalaoNF.codigo)
TalaoNF.codigo = 'NF12345'
print(TalaoNF.codigo)   
TalaoNF.codigo = 'NF123456'
print(TalaoNF.codigo)       
  