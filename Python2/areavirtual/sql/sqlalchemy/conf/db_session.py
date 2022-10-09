import sqlalchemy as sa
# Criar sessões
from sqlalchemy.orm import sessionmaker
# No SqLite3 para criar pastas e arquivos 
from pathlib import Path
# Para tipagem de dados
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.future.engine import Engine
# Para definição das Tabelas no BD (DDL), caso necessário.
from Models.model_base import ModelBase

# Variável Global da engine do BD
__engine: Optional[Engine] = None

def create_engine(sqlite:bool = True) -> Engine:
    """
        Criar a configuração ao BD
    """
    global __engine
    
    if __engine is None:
        if sqlite:
            arquivo_db = "db/estoque.sqlite" #estoque.db
            # Criar o banco no diretório (pasta) Pai
            folder = Path(arquivo_db).parent
            print("*** Folder: ", folder)
            folder.mkdir(parents=True, exist_ok=True)
            # String de conexão do banco
            conn_str = f"sqlite:///{arquivo_db}"
            # Versões antigas do PySqLite n permitiam conexões em multithreads, isso agiliza agora.
            __engine = sa.create_engine(url=conn_str, echo=False, connect_args={"check_same_thread":False})
    return __engine

def create_session() -> Session:
    """
        Criar a sessão de conexão ao BD
    """
    global __engine

    if not __engine:
        create_engine(sqlite=True)
    
    __session = sessionmaker(__engine, expire_on_commit=False, class_=Session)
    session: Session = __session()

def create_tables() -> None:
    """
        Criar as tabelas do BD
    """
    global __engine

    if not __engine:
        create_engine()
    import Models.__all_models
    ModelBase.metadata.drop_all(__engine)
    ModelBase.metadata.create_all(__engine)
