from acessoSuperMercado import Fornecedores, Produtos
import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///materiais.db',echo=False)
from sqlalchemy.orm import declarative_base
Base = declarative_base()


def incluirforn():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    novoforn = Fornecedores(id=int(input('Digite o id')),\
                                nome=input('Digite o nome'),\
                                    email=input('Digite o email'))
    sessao.add(novoforn)
    sessao.commit()
def excluirforn():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    excluir = sessao.query(Fornecedores).filter(Fornecedores.nome==input('Digite o nome que quer apagar')).first()
    if excluir != None:
        sessao.delete(excluir)
        sessao.commit()
def incluirprod():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    novoprod = Produtos(id=int(input('Digite o id')),\
                            desc=input('Digite a descrição'),\
                                id_fornprod=int(input('Digite o id do fornecedor do produto')))
    sessao.add(novoprod)
    sessao.commit()
def excluirprod():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    excluir1 = sessao.query(Produtos).filter(Produtos.desc==input('Digite a descrição do produto que quer apagar')).first()
    if excluir1 != None:
        sessao.delete(excluir1)
        sessao.commit()
def verforn():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    resposta = sessao.query(Fornecedores)
    for resp in resposta:
        print(resp.nome,\
                        resp.id)
def verprod():
    from sqlalchemy.orm import sessionmaker
    SessaoBD = sessionmaker(bind=engine)
    sessao = SessaoBD()
    resposta = sessao.query(Produtos)
    for resp in resposta:
            print(resp.desc,\
                        resp.id)

Base.metadata.create_all(engine) 

