class Compras:
    
    def __init__( self ):
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
        
        print( "O item " + item['nome'] + " foi adicionado à lista!" )


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
                print( "Removemos " + str( quantidade_removida ) + " " + item['nome'] + " da lista! (" + str( restantes ) + " itens restantes)" )
            else:
                # Limpamos completamente o item do dicionário de compras
                del self.dicionario_compras[ id ]
                print( "O item " + item['nome'] + " foi removido completamente da lista!" )


    # Termina as compras com um determinado pagamento
    def finaliza( self, pagamento ):
        total = 0

        # Repetição para mostrar todos os elementos da lista
        for codigo in self.dicionario_compras:
            produto = self.dicionario_compras[ codigo ]['produto']
            preco = produto['preço']
            quantidade = self.dicionario_compras[ codigo ]['quantidade']

            total += preco * quantidade

        print( "Total: " + str( total ) )
        
        if pagamento < total:
            print( "Dinheiro insuficiente!" )
            return False

        troco = pagamento - total

        if troco > 0:
            print( "Troco: " + str( troco ) )

        print( "Compra finalizada!" )

        self.dicionario_compras.clear()
        return True


    # Função para mostrar alguma lista na linha de comando
    def mostra( self ):
        
        # OOOOOOOOOOOOOOOOOOOO
        # ====================
        # Compras
        # --------------------
        # - (Mx) Item 1 R$ xxx
        # - (Mx) Item 2 R$ xxx
        # - ...
        # - (Mx) Item N R$ xxx
        #
        # --------------------
        # Total: R$ yyy
        # ====================

        print( "OOOOOOOOOOOOOOOOOOOO" )
        print( "====================" )
        print( "Compras" )
        print( "--------------------" )

        total = 0

        # Repetição para mostrar todos os elementos da lista
        for codigo in self.dicionario_compras:
            produto = self.dicionario_compras[ codigo ]['produto']
            preco = produto['preço']
            quantidade = self.dicionario_compras[ codigo ]['quantidade']

            # Mostra o elemento com um tracinho ao lado
            print( "- (" + str( quantidade ) + "x) " + produto['nome'] + ' R$' + str( preco ) )

            total += preco * quantidade

        print( "--------------------" )
        print( "" )
        print( "Total: R$" + str( total ) )
        print( "====================" )
