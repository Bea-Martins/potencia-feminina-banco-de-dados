import sqlite3

conexao = sqlite3.connect('banco') #conexão do arquivo python com o banco de dados
cursor = conexao.cursor() #passando o cursor pra uma nova variável

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora","França","isa@gmail.com",123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Maria","Itália","mari@gmail.com",654321)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(3,"João","Brasil","jo@gmail.com",123654)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(4,"José","Canadá","ze@gmail.com",654123)')
#cursor.execute('DELETE FROM usuario WHERE id=4')
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="João"')

# ORDER BY e DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome, id DESC') # * seleciona todas as colunas da tabela

# LIMIT e DISTINCT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')

# GROUP BY e HAVING
dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')
for usuario in dados:
  print(usuario)

cursor.execute('')
conexao.commit() #enviadas as informações
conexao.close #não da conflito na execução