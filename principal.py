import locale
import time

from aplicacao import Aplicacao
from interface import cria_janela_pesquisa, limpa_terminal, window
from PySimpleGUI import WINDOW_CLOSED

locale.setlocale( locale.LC_TIME, "pt_BR" )

app = Aplicacao()

# Laço principal
while app.executando:
    
    event, values = window.read( timeout=1000 )

    window['-TXT-CAB-']( time.strftime("%a, %d %b %Y %H:%M:%S") )
    
    if event == WINDOW_CLOSED or event == '-BTN-SAIR-':
        app.executando = False

    elif event == "-BTN-ADC-":
        try:
            id_produto = values['-COD-ADC-']
            quantidade = values['-QTD-ADC-']
            # Controller
            app.adiciona_compra( id_produto, quantidade )
            app.mostra_compras( window )
            window['-ERR-ADC-']('')
        except Exception as err:
            window['-ERR-ADC-']('Erro: ' + str( err ))

        window['-COD-ADC-']('')
        window['-QTD-ADC-']('')

    elif event == "-BTN-REM-":
        try:
            id_produto = values['-COD-REM-']
            quantidade = values['-QTD-REM-']
            # Controller
            app.remove_compra( id_produto, quantidade )
            app.mostra_compras( window )
            window['-ERR-REM-']('')
        except Exception as err:
            window['-ERR-REM-']('Erro: ' + str( err ))

        window['-COD-REM-']('')
        window['-QTD-REM-']('')

    elif event == '-BTN-REM-TUDO-':
        app.compras.dicionario_compras.clear()
        limpa_terminal()

    elif event == "-BTN-PGTO-":
        try:
            valor = values['-VAL-PGTO-']
            # Controller
            app.finaliza_compra( valor, window )
            window['-ERR-PGTO-']('')
            window['-SUC-PGTO-']('Pagamento realizado!')
        except Exception as err:
            window['-ERR-PGTO-']('Erro: ' + str( err ))

        window['-VAL-PGTO-']('')

    elif event == '-BTN-FIN-':
        if app.compras.finalizado:
            limpa_terminal()

    elif event == "-BTN-PESQ-":
        janela_pesquisa = cria_janela_pesquisa()
        while True:
            pesq_event, pesq_values = janela_pesquisa.read()
            
            if pesq_event == '-BTN-PESQ-':
                ordenacao = list( filter( lambda key: pesq_values[key], pesq_values ) )[0] # Desculpa
                app.busca_produtos( ordenacao, janela_pesquisa )
            
            if pesq_event == WINDOW_CLOSED or pesq_event == '-BTN-SAIR-':
                break
        janela_pesquisa.close()


window.close()

print( "Até logo :)" )
