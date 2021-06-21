import json

def busca_produtos_do_banco( caminho ):
    with open( caminho, 'r', encoding='utf-8' ) as file:
        dicionario = {}
        array = json.loads( file.read() )
        for produto in array:
            dicionario[ produto['código'] ] = produto
            
        return dicionario


def produto_existe( codigo ):
    return codigo in codigo_produtos


# Função para adicionar um item na lista
def adicionar_item( dicionario ):

    codigo_item = int( input( "Qual o código do item? " ) )

    if not produto_existe( codigo_item ):
        print( "O código " + str( codigo_item ) + " não existe na base de dados!" )
        return

    quantidade = int( input( "Quantos itens você gostaria de adicionar? " ) )

    if codigo_item in dicionario:
        # Adiciona um item ao que já existe
        dicionario[ codigo_item ] += quantidade
    else:
        dicionario[ codigo_item ] = quantidade
    
    produto = codigo_produtos[ codigo_item ]
    print( "O item " + produto['nome'] + " foi adicionado à lista!" )


# Função para remover um item da lista
def remover_item( dicionario ):

    # Busca o código do item
    codigo_item = int( input( "Qual o código do item que você deseja excluir? " ) )

    if not produto_existe( codigo_item ):
        print( "O código " + str( codigo_item ) + " não existe na base de dados!" )
        return

    # Se existe a compra no nosso dicionário
    if codigo_item in dicionario:
        # Busca os dados do produto
        produto = codigo_produtos[ codigo_item ]

        quantidade_removida = int( input( "Quantos itens você gostaria de remover? " ) )
        # Pegamos a quantidade de itens existentes
        quantidade_existente = dicionario[codigo_item]
        
        # Calculamos a quantidade de itens restantes
        restantes = quantidade_existente - quantidade_removida

        # Caso a quantidade seja maior do que 1
        if restantes >= 1:
            # Diminuímos em 1 a quantidade
            dicionario[codigo_item] = restantes
            print( "Removemos " + str( quantidade_removida ) + " " + produto['nome'] + " da lista! (" + str( restantes ) + " itens restantes)" )
        else:
            # Limpamos completamente o item do dicionário de compras
            del dicionario[codigo_item]
            print( "O item " + produto['nome'] + " foi removido completamente da lista!" )

    else:
        print( "Aviso: O item não existe na lista de compras!" )


# Função para mostrar alguma lista na linha de comando
def mostra_dicionario( dicionario ):
    
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
    for codigo in dicionario:
        produto = codigo_produtos[ codigo ]
        preco = produto['preço']
        quantidade = dicionario[ codigo ]

        # Mostra o elemento com um tracinho ao lado
        print( "- (" + str( quantidade ) + "x) " + produto['nome'] + ' R$' + str( preco ) )

        total += preco * quantidade

    print( "--------------------" )
    print( "" )
    print( "Total: R$" + str( total ) )
    print( "====================" )


def finaliza_compra( dicionario ):
    total = 0

    # Repetição para mostrar todos os elementos da lista
    for codigo in dicionario:
        produto = codigo_produtos[ codigo ]
        preco = produto['preço']
        quantidade = dicionario[ codigo ]

        total += preco * quantidade

    print( "Total: " + str( total ) )
    
    pagamento = int( input( "Quantidade em dinheiro para o pagamento: " ) )
    
    if pagamento < total:
        print( "Dinheiro insuficiente!" )
        return

    troco = pagamento - total

    if troco > 0:
        print( "Troco: " + str( troco ) )

    print( "Compra finalizada!" )

    dicionario.clear()


def mostra_produtos():

    opcoes = {
        '1': 'código',
        '2': 'nome',
        '3': 'preço'
    }

    for opcao in opcoes:
        print( str(opcao) + ": " + opcoes[opcao] )

    ordenacao = input( "Ordenar por qual campo? " )

    if ordenacao not in opcoes:
        print( "Opção inválida!" )
        return

    campo = opcoes[ordenacao]

    lista = []

    for codigo in codigo_produtos:
        lista.append( codigo_produtos[codigo] )
    
    lista.sort( key=lambda produto: produto[campo] )
    
    for produto in lista:
        print( "[" + str( produto['código'] ) + "] " + produto['nome'] + ' R$' + str( produto['preço'] ) )


# Banco de dados dos produtos
codigo_produtos = busca_produtos_do_banco( 'bancodedados.json' )
# Inicialização da lista
dicionario_de_compras = {}


# Laço principal
while True:

    entrada = input( "Qual comando você gostaria de executar? " )

    if entrada == "adicionar":
        adicionar_item( dicionario_de_compras )

    elif entrada == "remover":
        remover_item( dicionario_de_compras )

    elif entrada == "mostrar":
        mostra_dicionario( dicionario_de_compras )

    elif entrada == "finalizar":
        finaliza_compra( dicionario_de_compras )

    elif entrada == "produtos":
        mostra_produtos()

    elif entrada == "sair":
        break

    else:
        print( "Comando não encontrado!" )


print( "Até logo :)" )
