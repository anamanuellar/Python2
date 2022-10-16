from conf.db_session import create_session
from Models.cliente import Cliente 

def lista_clientes() -> None:
    try:
        with create_session() as session:
            # Retorna um objeto
            # listaCliente:List[Cliente] = session.query(Cliente)
            
            # Retorna uma lista
            listaCliente = session.query(Cliente).order_by(Cliente.matricula.desc()).all()
            for cli in listaCliente:
                print(f"Codigo: {cli.matricula}")
                print(f"Nome: {cli.nome}")
            
        session.commit()
    except:
        print("Erro ao consultar Clientes!")


lista_clientes()
