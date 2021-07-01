from banco_de_dados import BancoDeDados
from compras import Compras

class Aplicacao:
    def __init__( self ):
        self.banco = BancoDeDados( 'bancodedados.json' )
        self.compras = Compras()
        self.lista_produtos = []
        self.executando = True

    def adiciona_compra( self, id_produto, quantidade ):
        # Conversão de dados
        try:
            id_produto = int( id_produto )
            quantidade = int( quantidade )
        except:
            raise Exception( 'Valor(es) inválido(s)' )

        if not self.banco.produto_existe( id_produto ):
            raise Exception( 'Não existe produto com o código informado!' )

        # Chamar as models
        produto = self.banco.pesquisa_produto( id_produto )
        self.compras.adicionar_item( produto, quantidade )


    def remove_compra( self, id_produto, quantidade ):
        # Conversão/validação de dados
        try:
            id_produto = int( id_produto )
            quantidade = int( quantidade )
        except:
            raise Exception( 'Valor(es) inválido(s)' )

        if not self.compras.esta_nas_compras( id_produto ):
            raise Exception( 'Não há compra com o código informado!' )
        
        # Chamar as models
        self.compras.remover_item( id_produto, quantidade )


    def mostra_compras( self, window ):
        # Pega os valores
        lista, total = self.compras.mostra()
        # Atualiza a tela
        window['-COMPRAS-'].update( lista )
        window['-TXT-TOTAL-'].update( 'Total: R$ ' + str(total) )


    def finaliza_compra( self, valor, window ):
        # Conversão de dados
        try:
            valor = int( valor )
        except:
            raise Exception( 'Valor inválido!' )
        
        # Validação
        if valor <= 0:
            raise Exception( 'Valor precisa ser positivo!' )

        # Chamar as models
        troco = self.compras.finaliza( valor )
        
        window['-TXT-TROCO-'].update( 'Troco: R$' + str( troco ) )


    # Valida os dados e busca os produtos do banco
    def busca_produtos( self, tipo_ordenacao, window ):
        if not BancoDeDados.valida_ordenacao( tipo_ordenacao ):
            raise Exception( 'Valor de ordenação inválido!' )
        # Busca dados dos produtos e os textos para visualização
        produtos, produtos_str = self.banco.mostra_produtos( tipo_ordenacao )
        self.lista_produtos = produtos
        window['-PRODUTOS-']( produtos_str )

    def atualiza_produto( self, produto ):
        try:
            codigo = int( produto['código'] )
            nome = produto['nome']
            preco = int( produto['preço'] )
        except:
            raise Exception( 'Valor(es) inválido(s)!' )

        self.banco.atualiza_produto( codigo, nome, preco )

    def adiciona_produto( self, produto ):
        try:
            nome = produto['nome']
            preco = int( produto['preço'] )
        except:
            raise Exception( 'Valor(es) inválido(s)!' )
        
        self.banco.adiciona_produto( nome, preco )


    def autentica( self, chave ):
        if not self.banco.autentica( chave ):
            raise Exception( 'Chave incorreta!' )

    # Sai da aplicação
    def sair( self ):
        self.executando = False
        