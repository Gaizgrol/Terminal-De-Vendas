import sqlite3

conexao = sqlite3.connect( 'banco.sqlite' )

class BancoDeDados:

    ORDENAR_CODIGO = '1'
    ORDENAR_NOME = '2'
    ORDENAR_PRECO = '3'

    opcoes = {
        ORDENAR_CODIGO: 'código',
        ORDENAR_NOME: 'nome',
        ORDENAR_PRECO: 'preço'
    }

    def valida_ordenacao( id_ordenacao ):
        if id_ordenacao not in BancoDeDados.opcoes:
            return False
        return True
    
    def __init__( self, caminho ):
        self.cursor = conexao.cursor()
        self.caminho = caminho
        self.codigo_produtos = self.busca_produtos_do_banco( caminho )

    def busca_produtos_do_banco( self, caminho ):
        
        self.cursor.execute( '''SELECT rowid, * FROM produtos''' )
        tabela = self.cursor.fetchall()
        
        dicionario = {}
        for produto in tabela:
            codigo, nome, preco = produto
            dicionario[ codigo ] = {
                'código': codigo,
                'nome': nome,
                'preço': preco
            }

        return dicionario

    def salvar_produtos_do_banco( self ):
        conexao.commit()


    def produto_existe( self, codigo ):
        return codigo in self.codigo_produtos


    def mostra_produtos( self, ordenacao ):
        campo = BancoDeDados.opcoes[ordenacao]

        lista = []

        for codigo in self.codigo_produtos:
            lista.append( self.codigo_produtos[codigo] )
        
        lista.sort( key=lambda produto: produto[campo] )
        
        lista_str = []

        for produto in lista:
            lista_str.append( "[" + str( produto['código'] ) + "] " + produto['nome'] + ' R$' + str( produto['preço'] ) )

        return ( lista, lista_str )


    def pesquisa_produto( self, codigo ):
        return self.codigo_produtos[ codigo ]

    def atualiza_produto( self, codigo, nome, preco ):
        self.cursor.execute( 'UPDATE produtos SET nome = ?, preco = ? WHERE rowid = ?', ( nome, preco, codigo ))
        self.salvar_produtos_do_banco()

        produto = self.codigo_produtos[ codigo ]
        produto['nome'] = nome
        produto['preço'] = preco

    def adiciona_produto( self, nome, preco ):
        self.cursor.execute('INSERT INTO produtos VALUES (?,?)', ( nome, preco ))
        codigo = self.cursor.lastrowid
        self.salvar_produtos_do_banco()
        produto = {
            'código': codigo,
            'nome': nome,
            'preço': preco
        }
        self.codigo_produtos[ codigo ] = produto

    def autentica( self, chave ):
        return chave == '123'
        