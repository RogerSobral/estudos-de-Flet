from sqlalchemy import (Column, Integer, String,DOUBLE,
                        DATE,BOOLEAN,ForeignKey)
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Income(Base):
    __tablename__="income"
    id= Column(Integer,primary_key=True,autoincrement=True,unique=True)
    descricao=Column(String, nullable=False)
    valor=Column(DOUBLE, nullable=False)
    data_vencimento=Column(DATE)
    realizada=Column(BOOLEAN)
    id_categoria=Column(Integer,ForeignKey("category.id"), nullable=False)
    id_conta=Column(Integer, ForeignKey("account.id"),nullable=False)




