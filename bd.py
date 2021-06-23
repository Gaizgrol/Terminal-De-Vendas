import json



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
    
    def mostra_ordenacoes():
        opcoes = BancoDeDados.opcoes
        for opcao in opcoes:
            print( opcao + ': ' + opcoes[opcao] )

    def __init__( self, caminho ):
        self.codigo_produtos = self.busca_produtos_do_banco( caminho )

    # Método interno
    def busca_produtos_do_banco( self, caminho ):
        with open( caminho, 'r', encoding='utf-8' ) as file:
            dicionario = {}
            array = json.loads( file.read() )
            for produto in array:
                dicionario[ produto['código'] ] = produto
                
            return dicionario

    def produto_existe( self, codigo ):
        return codigo in self.codigo_produtos

    def mostra_produtos( self, ordenacao ):
        
        campo = BancoDeDados.opcoes[ordenacao]

        lista = []

        for codigo in self.codigo_produtos:
            lista.append( self.codigo_produtos[codigo] )
        
        lista.sort( key=lambda produto: produto[campo] )
        
        for produto in lista:
            print( "[" + str( produto['código'] ) + "] " + produto['nome'] + ' R$' + str( produto['preço'] ) )

    def pesquisa_produto( self, codigo ):
        return self.codigo_produtos[ codigo ]