from bd import BancoDeDados
from compras import Compras

class Aplicacao:
    def __init__( self ):
        self.banco = BancoDeDados( 'bancodedados.json' )
        self.compras = Compras()
        self.executando = True

    def adiciona_compra( self, id_produto, quantidade ):
        # Conversão/validação de dados
        id_produto = int( id_produto )
        quantidade = int( quantidade )
        if not self.banco.produto_existe( id_produto ):
            print( 'Não encontramos o produto com o código informado!' )
            return
        # Chamar as models
        produto = self.banco.pesquisa_produto( id_produto )
        self.compras.adicionar_item( produto, quantidade )


    def remove_compra( self, id_produto, quantidade ):
        # Conversão/validação de dados
        id_produto = int( id_produto )
        quantidade = int( quantidade )
        if not self.compras.esta_nas_compras( id_produto ):
            print( 'Não encontramos a compra do produto com o código informado!' )
            return
        # Chamar as models
        self.compras.remover_item( id_produto, quantidade )


    def mostra_compras( self ):
        # Chamar as models
        self.compras.mostra()


    def finaliza_compra( self, valor ):
        # Conversão/validação de dados
        valor = int( valor )
        if valor <= 0:
            print( 'Valor inválido!' )
            return
        # Chamar as models
        self.compras.finaliza( valor )


    # Valida os dados e busca os produtos do banco
    def busca_produtos( self, tipo_ordenacao ):
        if not BancoDeDados.valida_ordenacao( tipo_ordenacao ):
            print( 'Valor de ordenação inválido!' )
            BancoDeDados.mostra_ordenacoes()
            return
        # Chamar as models
        self.banco.mostra_produtos( tipo_ordenacao )


    # Sai da aplicação
    def sair( self ):
        self.executando = False