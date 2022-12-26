import sqlalchemy
engine = sqlalchemy.create_engine('sqlite:///materiais.db',echo=False)
from sqlalchemy.orm import declarative_base
Base = declarative_base()
from sqlalchemy import Column, String, Integer, ForeignKey

class Fornecedores(Base):
    __tablename__ = 'tab_fornecedores'
    id = Column(Integer, primary_key=True)
    nome = Column(String(20))
    email = Column(String(20))
    fone = Column(Integer)

class Produtos(Base):
    __tablename__ = 'tab_produtos'
    id = Column(Integer, primary_key=True)
    desc = Column(String(20))
    id_fornprod = Column(Integer,ForeignKey('tab_fornecedores.id'))

Base.metadata.create_all(engine)