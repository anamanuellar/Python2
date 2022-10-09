from conf.db_session import create_session
from Models.cliente import Cliente

def inserir_cliente() -> None:
    print("Cadastro de Cliente")

    vMatricula:int = int(input("Informe o Código do Cliente: "))
    vNome:str = input("Informe o Nome do Cliente: ")
    vEndereco:str = input("Informe o Endereço de Cobrança: ")
    vEmail:str = input("Informe o Email do Cliente: ")
    vTelefone:str = input("Informe o Telefone de contato: ")

    cli:Cliente = Cliente(
        matricula=vMatricula,
        nome=vNome,
        endereco=vEndereco,
        email=vEmail,
        telefone=vTelefone
    )

    # Trabalhando com Contexto: (Context Manager)
    with create_session() as session:
        session.add(cli)
        # Efetue todas as operações, ao final...
        session.commit()
    
    print("Cliente cadastrado com sucesso")    
    print(f"ID: {cli.codigo}, NOME: {cli.nome}")
