from conta import Contas

contaBradesco = Contas("Ana", "1234-5", False)
print(contaBradesco.titular)
print(contaBradesco.saldo)
print(contaBradesco.depositar(20))
print(contaBradesco.extrato())
if print(contaBradesco.sacar(32)):
    print(contaBradesco.saldo)
else:
    print('Saldo insuficiente')
    
print(contaBradesco.extrato())