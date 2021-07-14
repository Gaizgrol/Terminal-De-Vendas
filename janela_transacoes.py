import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED

class JanelaTransacoes:

    def __init__( self, app ):
        self.app = app
        self.compras, self.compras_str = self.app.banco.busca_compras()
        self.window = sg.Window( 'Histórico de compras', layout=[
            [ sg.Text( 'Histórico:' ) ],
            [
                sg.Listbox( self.compras_str, enable_events=True, size=(32, 10), key='-HISTORICO-' ),
                sg.Listbox( [], size=(64, 10), key='-TRANSACOES-' )
            ],
            [
                sg.Text( '', size=(32, None) ),
                sg.Text( 'Valor:', size=(64, None), key='-TXT-VALOR-' )
            ],
            [
                sg.Text( '', size=(32, None) ),
                sg.Text( 'Pago:', size=(64, None), key='-TXT-PAGO-' )
            ],
            [
                sg.Text( '', size=(32, None) ),
                sg.Text( 'Troco:', size=(64, None), key='-TXT-TROCO-' )
            ],
            [ sg.Button( 'Voltar', button_color='red', key='-BTN-CANCELAR-' ) ]
        ])
        self.loop()
        self.fechar()

    def loop( self ):
        while True:
            event, values = self.window.read()

            if event == WINDOW_CLOSED or event == '-BTN-CANCELAR-':
                break

            if event == '-HISTORICO-':
                posicao = self.window['-HISTORICO-'].get_indexes()[0]
                compra = self.compras[ posicao ]
                transacoes, transacoes_str = self.app.banco.busca_transacoes( compra['código'] )
                self.window['-TRANSACOES-']( transacoes_str )

                preco = 0
                for transacao in transacoes:
                    preco += transacao['preço_produto'] * transacao['qtd_produto']

                self.window['-TXT-VALOR-']( 'Valor: R$' + str( preco ) )
                self.window['-TXT-PAGO-']( 'Pago: R$' + str( compra['pago'] ) )
                self.window['-TXT-TROCO-']( 'Troco: R$' + str( compra['pago'] - preco ) )

    def fechar( self ):
        self.window.close()
