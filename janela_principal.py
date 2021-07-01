from PySimpleGUI import WINDOW_CLOSED
from janela_produtos import JanelaProdutos
import PySimpleGUI as sg
import time

class JanelaPrincipal:

    def __init__( self, app ):
        self.app = app
        self.window = sg.Window( 'Terminal', layout=[
            # Cabeçalhp
            [ sg.Text( '', size=( 32, None ), key='-TXT-CAB-' ) ],

            [ sg.Text( '______________________________________________________________', text_color='white' ) ],

            # Menu geral
            [ sg.Button( 'Pesquisar produtos', key='-BTN-PESQ-' ), sg.Button( 'Sair', button_color='red', key='-BTN-SAIR-' ) ],

            [ sg.Text( '______________________________________________________________', text_color='white' ) ],

            # Lista de compras
            [ sg.Text( 'Compras:' ) ],
            [ sg.Listbox( [], size=(32, 10), key='-COMPRAS-', enable_events=True ) ],

            # Texto relacionado ao dinheiro
            [ sg.Text( '', size=( 16, None ), key='-TXT-TOTAL-' ) ],
            [ sg.Text( '', size=( 16, None ), key='-TXT-TROCO-' ) ],
            
            # Linha de entrada de produtos
            [
                sg.Text( 'Código:' ),
                sg.InputText( size=( 4, None ), key='-COD-ADC-' ),
                sg.Text( 'Quantidade:' ),
                sg.InputText( size=( 8, None ), key='-QTD-ADC-' ),
                sg.Button( 'Adicionar', key='-BTN-ADC-' )
            ],
            [ sg.Text( '', size=(48,None), text_color='red', key='-ERR-ADC-' ) ],
            
            # Linha de remoção de produtos
            [
                sg.Text( 'Código:' ),
                sg.InputText( size=( 4, None ), key='-COD-REM-' ),
                sg.Text( 'Quantidade:' ),
                sg.InputText( size=( 8, None ), key='-QTD-REM-' ),
                sg.Button( 'Remover', key='-BTN-REM-' ),
                sg.Button( 'Remover tudo', key='-BTN-REM-TUDO-' )
            ],
            [ sg.Text( '', size=(48,None), text_color='red', key='-ERR-REM-' ) ],
            
            # Realizar pagamento
            [
                sg.InputText( size=( 10, None ), key='-VAL-PGTO-' ),
                sg.Button( 'Pagar', key='-BTN-PGTO-' ),
                sg.Text( '', size=(32,None), text_color='white', key='-SUC-PGTO-' )
            ],
            [ sg.Text( '', size=(48,None), text_color='red', key='-ERR-PGTO-' ) ],
            
            # Resetar compras
            [ sg.Button( 'Finalizar', key='-BTN-FIN-' ) ]
        ])
        self.loop()
        self.fechar()

    def loop( self ):

        while self.app.executando:
            event, values = self.window.read( timeout=1000 )

            # Atualiza o cabeçalho
            self.window['-TXT-CAB-']( time.strftime("%a, %d %b %Y %H:%M:%S") )
            
            if event == WINDOW_CLOSED or event == '-BTN-SAIR-':
                self.app.executando = False

            elif event == "-BTN-ADC-":
                try:
                    id_produto = values['-COD-ADC-']
                    quantidade = values['-QTD-ADC-']
                    # Controller
                    self.app.adiciona_compra( id_produto, quantidade )
                    self.app.mostra_compras( self.window )
                    self.window['-ERR-ADC-']('')
                except Exception as err:
                    self.window['-ERR-ADC-']('Erro: ' + str( err ))

                self.window['-COD-ADC-']('')
                self.window['-QTD-ADC-']('')

            elif event == "-BTN-REM-":
                try:
                    id_produto = values['-COD-REM-']
                    quantidade = values['-QTD-REM-']
                    # Controller
                    self.app.remove_compra( id_produto, quantidade )
                    self.app.mostra_compras( self.window )
                    self.window['-ERR-REM-']('')
                except Exception as err:
                    self.window['-ERR-REM-']('Erro: ' + str( err ))

                self.window['-COD-REM-']('')
                self.window['-QTD-REM-']('')

            elif event == '-BTN-REM-TUDO-':
                self.app.compras.dicionario_compras.clear()
                self.limpa_terminal()

            elif event == "-BTN-PGTO-":
                try:
                    valor = values['-VAL-PGTO-']
                    # Controller
                    self.app.finaliza_compra( valor, self.window )
                    self.window['-ERR-PGTO-']('')
                    self.window['-SUC-PGTO-']('Pagamento realizado!')
                except Exception as err:
                    self.window['-ERR-PGTO-']('Erro: ' + str( err ))

                self.window['-VAL-PGTO-']('')

            elif event == '-BTN-FIN-':
                if self.app.compras.finalizado:
                    self.limpa()

            elif event == "-BTN-PESQ-":
                JanelaProdutos( self.app )

    def limpa( self ):

        keys = [
            '-TXT-TOTAL-', '-TXT-TROCO-',
            '-COD-ADC-', '-QTD-ADC-', '-ERR-ADC-',
            '-COD-REM-', '-QTD-REM-', '-ERR-REM-',
            '-VAL-PGTO-', '-SUC-PGTO-', '-ERR-PGTO-'
        ]

        self.window['-COMPRAS-'].update([])
        for key in keys:
            self.window[key]('')

    def fechar( self ):
        self.window.close()