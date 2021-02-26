from sqlalchemy import (create_engine, String, Integer,Column,Table,MetaData)
engine = creat_engine('sqlite:///banco.db', echo=True)
metadata = MetaData(bind=engine)

tabela_pessoa = Table("pessoa", metadata,
                      Column("id", Integer , primary_key=True),
                      Column("nome",String(40)),
                      Column("idade",Integer))

metadata.create_all()