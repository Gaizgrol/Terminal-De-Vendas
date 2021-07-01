import sqlite3

conexao = sqlite3.connect('banco.sqlite')

cursor = conexao.cursor()
cursor.execute( 'DROP TABLE IF EXISTS produtos' )
cursor.execute( 'CREATE TABLE produtos (nome text, preco integer)' )
cursor.executemany( 'INSERT INTO produtos VALUES (?, ?)', [
    ( 'Óleo de soja (700ml)', 7 ),
    ( 'Vassoura Un.', 10 ),
    ( 'Arroz Integral (5kg)', 9 ),
    ( 'Brócolis Un.', 2 ),
    ( 'Aveia (700g)', 4 ),
    ( 'Banana (kg)', 4 ),
    ( 'Batata (kg)', 5 ),
    ( 'Cenoura (kg)', 4 ),
    ( 'Alface (Un.)', 2 ),
    ( 'Bicicleta BRA-B4 Aro 28"', 599 )
])

conexao.commit()
