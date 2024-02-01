import sqlite3

conexao = sqlite3.connect('banco') #conexão do arquivo python com o banco de dados
cursor = conexao.cursor() #passando o cursor pra uma nova variável

#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('CREATE TABLE gerentes(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')
#cursor.execute('DROP TABLE produtos')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(1,"Isadora","França","isa@gmail.com",123456)')
#cursor.execute('INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES(2,"Maria","Itália","mari@gmail.com",654321)')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(3,"João","Brasil","jo@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(4,"José","Canadá","ze@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(1,"Beatriz","Canadá","bea@gmail.com")')
#cursor.execute('INSERT INTO gerentes(id,nome,endereco,email) VALUES(2,"Camila","Florianópolis","mila@gmail.com")')
#cursor.execute('DELETE FROM usuario WHERE id=4')
#cursor.execute('UPDATE usuario SET endereco="Minas Gerais" WHERE nome="João"')
# cursor.execute('UPDATE gerentes SET id=7 WHERE nome="Beatriz"')
# cursor.execute('UPDATE gerentes SET id=9 WHERE nome="Camila"')

# ORDER BY e DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome, id DESC') # * seleciona todas as colunas da tabela

# LIMIT e DISTINCT
#dados = cursor.execute('SELECT DISTINCT * FROM usuario LIMIT 3')

# GROUP BY e HAVING
#dados = cursor.execute('SELECT nome FROM usuario GROUP BY nome HAVING id>3')

# JOIN's
# JOIN - INNER JOIN
#dados = cursor.execute('SELECT * FROM usuario INNER JOIN gerentes ON usuario.id = gerentes.id')

# JOIN - LEFT JOIN
#dados = cursor.execute('SELECT * FROM usuario LEFT JOIN gerentes ON usuario.id = gerentes.id')

# JOIN - RIGHT JOIN
#dados = cursor.execute('SELECT * FROM usuario RIGHT JOIN gerentes ON usuario.nome = gerentes.nome')

# JOIN - FULL JOIN
#dados = cursor.execute('SELECT * FROM usuario FULL JOIN gerentes ON usuario.nome = gerentes.nome')

# SUB-CONSULTAS
dados = cursor.execute('SELECT * FROM usuario WHERE nome IN (SELECT nome FROM gerentes)')
for usuario in dados:
  print(usuario)

cursor.execute('')
conexao.commit() #enviadas as informações
conexao.close #não da conflito na execução