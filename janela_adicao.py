import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED

class JanelaAdicao:

    def __init__( self, app ):
        self.app = app
        self.modificado = False
        self.window = sg.Window( 'Adicionar produto', layout=[
            [ sg.Text( 'Informações:' )],
            [
                sg.Text( 'Chave de admin:' ),
                sg.InputText( key='-VAL-ADM-' ),
            ],
            [
                sg.Text( 'Nome:' ),
                sg.InputText( size=( 30, None ), key='-VAL-NOME-' ),
                sg.Text( 'Preço:' ),
                sg.InputText( size=( 8, None ), key='-VAL-PRC-' ),
            ],
            [ sg.Text( '', size=(40,None), text_color='red', key='-ERR-ATT-' ) ],
            [ sg.Button( 'Adicionar', key='-BTN-ADC-' ) ],
            [ sg.Button( 'Voltar', button_color='red', key='-BTN-CANCELAR-' ) ]
        ])
        self.loop()
        self.fechar()

    def loop( self ):
        while True:
            event, values = self.window.read()

            if event == WINDOW_CLOSED or event == '-BTN-CANCELAR-':
                break

            elif event == '-BTN-ADC-':
                chave = values['-VAL-ADM-']
                try:
                    self.app.autentica( chave )
                    nome = values['-VAL-NOME-']
                    preco = values['-VAL-PRC-']
                    self.app.adiciona_produto({
                        'nome': nome,
                        'preço': preco
                    })
                    self.window['-ERR-ATT-']('')
                    self.modificado = True
                except Exception as err:
                    self.window['-ERR-ATT-']( 'Erro: ' + str( err ) )

    def fechar( self ):
        self.window.close()
