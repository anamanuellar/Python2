import sqlalchemy as sa
from datetime import datetime
from Models.model_base import ModelBase


class Produto(ModelBase):
    __tablename__:str = "Produtos"

    codigo: int = sa.Column(sa.BigInteger, primary_key=True)
    nome: str = sa.Column(sa.VARCHAR(50), nullable=False)
    descricao:str = sa.Column(sa.VARCHAR(200), nullable=True)
    ano_fab:int = sa.Column(sa.INTEGER)
    preco:float = sa.Column(sa.DECIMAL(10,2), nullable=False)
    data_cad: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    def __repr__(self) -> str:
        return f"<{Produto}: {self.nome}>"   
    
'''
    Para testar:
    python
    Models.produto import Produto
    prod=(matricula=1, nome="Carlos Gomes")
    cli

'''