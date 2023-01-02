from acessoSuperMercado import Fornecedores, Produtos
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///materiais.db',echo=False)
from sqlalchemy.orm import declarative_base
Base = declarative_base()


def incluirforn():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    novoforn = Fornecedores(id=int(input('id')),\
                            nome=input('name'),\
                            email=input('email'))
    sessao.add(novoforn)
    sessao.commit()
def excluirforn():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    excluir = sessao.query(Fornecedores).filter(Fornecedores.nome==input('excprod')).first()
    if excluir != None:
        sessao.delete(excluir)
        sessao.commit()
def incluirprod():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    novoprod = Produtos(id=int(input('id')),\
                        desc=input('desc'),\
                        id_fornprod=int(input('idforn')))
    sessao.add(novoprod)
    sessao.commit()
def excluirprod():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    excluir1 = sessao.query(Produtos).filter(Produtos.desc==input('excprod')).first()
    if excluir1 != None:
        sessao.delete(excluir1)
        sessao.commit()
def verforn():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    resposta = sessao.query(Fornecedores)
    for resp in resposta:
        return resp.nome,\
                resp.id
def verprod():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    resposta = sessao.query(Produtos)
    for resp in resposta:
            return resp.desc,\
                    resp.id

Base.metadata.create_all(engine) 
