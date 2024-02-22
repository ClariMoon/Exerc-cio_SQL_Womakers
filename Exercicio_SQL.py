import sqlite3

conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

## Exercício 1
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(20));')

## Exercício 2
#cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (1, 'Maria', 20, 'Química'), (2, 'José', 28, 'Direito'), (3, 'Carla', 15, 'Letras'), (4, 'Luísa', 35, 'Medicina'), (5, 'Pedro', 40, 'Contabilidade');')

## Exercício 3
#cursor.execute(


#query = cursor.execute(' SELECT * FROM alunos')

#for aluno in query:
    #print(aluno)



conexao.commit()
conexao.close