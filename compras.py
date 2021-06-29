class Compras:
    
    def __init__( self ):
        self.finalizado = False
        self.dicionario_compras = {}

    def esta_nas_compras( self, id ):
        return id in self.dicionario_compras


    # Adiciona uma quantidade de itens nas compras
    def adicionar_item( self, item, quantidade_adicionada ):
        id = item['código']

        if id in self.dicionario_compras:
            # Adiciona a quantia atual
            self.dicionario_compras[ id ]['quantidade'] += quantidade_adicionada
        else:
            # Cria os dados das compras
            self.dicionario_compras[ id ] = {
                'quantidade': quantidade_adicionada,
                'produto': item
            }


    # Remove uma quantidade de itens das compras
    def remover_item( self, id, quantidade_removida ):
        # Se existe a compra no nosso dicionário
        if self.esta_nas_compras( id ):

            info_produto = self.dicionario_compras[ id ]
            item = info_produto['produto']

            # Pegamos a quantidade de itens existentes
            quantidade_existente = info_produto['quantidade']
            
            # Calculamos a quantidade de itens restantes
            restantes = quantidade_existente - quantidade_removida

            # Caso a quantidade seja maior do que 1
            if restantes >= 1:
                # Atualiza a quantidade de produtos restantes
                info_produto[ 'quantidade' ] = restantes
            else:
                # Limpamos completamente o item do dicionário de compras
                del self.dicionario_compras[ id ]


    # Termina as compras com um determinado pagamento
    def finaliza( self, pagamento ):
        total = 0

        # Repetição para mostrar todos os elementos da lista
        for codigo in self.dicionario_compras:
            produto = self.dicionario_compras[ codigo ]['produto']
            preco = produto['preço']
            quantidade = self.dicionario_compras[ codigo ]['quantidade']

            total += preco * quantidade

        if total == 0:
            raise Exception( 'Não há compras!' )
        
        if pagamento < total:
            raise Exception( 'Dinheiro insuficiente!' )

        troco = pagamento - total

        self.finalizado = True
        self.dicionario_compras.clear()

        return troco


    # Função para mostrar alguma lista na linha de comando
    def mostra( self ):
        
        total = 0
        lista = []

        # Repetição para mostrar todos os elementos da lista
        for codigo in self.dicionario_compras:
            produto = self.dicionario_compras[ codigo ]['produto']
            preco = produto['preço']
            quantidade = self.dicionario_compras[ codigo ]['quantidade']

            linha = "- (" + str( quantidade ) + "x) " + produto['nome'] + ' R$' + str( preco )
            lista.append( linha )

            total += preco * quantidade

        return ( lista, total )
