import datetime
import sqlite3

conexao = sqlite3.connect('banco.sqlite')

cursor = conexao.cursor()

# Deleta as tabelas
cursor.execute( 'DROP TABLE IF EXISTS transacoes' )
cursor.execute( 'DROP TABLE IF EXISTS produtos' )
cursor.execute( 'DROP TABLE IF EXISTS compras' )

# Cria as tabelas
cursor.execute( 'CREATE TABLE produtos (nome text, preco integer)' )
cursor.execute( 'CREATE TABLE compras (data timestamp, valor_pago integer)' )
cursor.execute( '''CREATE TABLE transacoes (
    rowid_produto integer,
    rowid_compra integer,
    preco_produto integer,
    qtd_produto integer,
    FOREIGN KEY (rowid_produto) REFERENCES produtos(rowid),
    FOREIGN KEY (rowid_compra) REFERENCES compras(rowid)
)''' )

# Seeders
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
