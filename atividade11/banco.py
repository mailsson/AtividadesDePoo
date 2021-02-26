from main import engine,tabela
connect = engine.connect()
insert = tabela_pessoa.insert()
pessoa = insert.values(nome="paulo cesar", idade=37)
pessoa02 = insert.values(nomw="humberto constantino", idade=22)
pessoa03 = insert.values(nome='mailson', idade=30)

connect.execute(pessoa)
connect.execute(pessoa02)
connect.execute(pessoa03)


