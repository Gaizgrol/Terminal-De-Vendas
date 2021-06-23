from aplicacao import Aplicacao

app = Aplicacao()

# Laço principal
while app.executando:

    entrada = input( "Qual comando você gostaria de executar? " )

    if entrada == "adicionar":
        id_produto = input( 'Qual o código do produto? ' )
        quantidade = input( 'Quanto gostaria de adicionar? ' )
        # Controller
        app.adiciona_compra( id_produto, quantidade )

    elif entrada == "remover":
        id_produto = input( 'Qual o código do produto? ' )
        quantidade = input( 'Quanto gostaria de remover? ' )
        # Controller
        app.remove_compra( id_produto, quantidade )

    elif entrada == "mostrar":
        # Controller
        app.mostra_compras()

    elif entrada == "finalizar":
        valor = input( 'Qual a quantia em dinheiro?' )
        # Controller
        app.finaliza_compra( valor )

    elif entrada == "produtos":
        tipo_ordenacao = input( 'Gostaria de ordenar os produtos de qual forma? ' )
        # Controller
        app.busca_produtos( tipo_ordenacao )

    elif entrada == "sair":
        # Controller
        app.sair()

    else:
        print( "Comando não encontrado!" )


print( "Até logo :)" )
