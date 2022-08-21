from conta import *


nome = input('Digite o nome do Titular: ')
conta = input ('Digite a conta: ')
contaBradesco = Contas(nome, conta)
cliente	=	Cliente('João',	'Oliveira',	'1111111111-1')

while(True):
    mov = input('1- Sacar ou 2-Depositar')
    valor = float(input('Informe o valor: '))
    if mov == '1':
        if( contaBradesco.sacar(valor)== False):
            print('Saldo insuficiente')
    else:
        contaBradesco.depositar(valor)
    print(contaBradesco.extrato(valor))


