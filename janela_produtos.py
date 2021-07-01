import PySimpleGUI as sg
from PySimpleGUI import WINDOW_CLOSED
from janela_adicao import JanelaAdicao

class JanelaProdutos:

    def __init__( self, app ):
        self.app = app
        self.codigo_selecionado = None
        self.window = sg.Window( 'Pesquisa', layout=[
            [ sg.Text( 'Ordenar por:' )],
            [
                sg.Radio( 'Código', 'ORDENACOES', True, key='1' ),
                sg.Radio( 'Nome', 'ORDENACOES', key='2' ),
                sg.Radio( 'Preço', 'ORDENACOES', key='3' )
            ],
            [ sg.Button( 'Pesquisar', key='-BTN-PESQ-' ) ],
            [ sg.Text( 'Produtos:' ) ],
            [ sg.Listbox([], size=(32, 10), enable_events=True, key='-PRODUTOS-') ],
            [ sg.Button( 'Adicionar produto', key='-ADICIONAR-' ) ],
            [ sg.Text( 'Produto selecionado:' ), sg.Text( '', size=( 40, None ), key='-TXT-COD-' ) ],
            [
                sg.Text( 'Nome:' ),
                sg.InputText( size=( 30, None ), key='-VAL-NOME-' ),
                sg.Text( 'Preço:' ),
                sg.InputText( size=( 8, None ), key='-VAL-PRC-' ),
            ],
            [ sg.Text( '', size=(40,None), text_color='red', key='-ERR-ATT-' ) ],
            [ sg.Button( 'Atualizar', key='-ATUALIZAR-' ) ],
            [ sg.Button( 'Voltar', button_color='red', key='-BTN-SAIR-' ) ]
        ])
        self.loop()
        self.fechar()

    def loop( self ):
        while True:
            pesq_event, pesq_values = self.window.read()

            if pesq_event == WINDOW_CLOSED or pesq_event == '-BTN-SAIR-':
                break
            
            elif pesq_event == '-BTN-PESQ-':
                self.pesquisa( pesq_values )
            
            elif pesq_event == '-PRODUTOS-':
                try:
                    posicao = self.window['-PRODUTOS-'].get_indexes()[0]
                    produto_selecionado = self.app.lista_produtos[ posicao ]
                    
                    self.codigo_selecionado = produto_selecionado['código']
                    self.window['-TXT-COD-']( self.codigo_selecionado )
                    self.window['-VAL-NOME-']( produto_selecionado['nome'] )
                    self.window['-VAL-PRC-']( produto_selecionado['preço'] )
                except:
                    pass

            elif pesq_event == '-ATUALIZAR-':
                produto = {
                    'código': self.codigo_selecionado,
                    'nome': pesq_values['-VAL-NOME-'],
                    'preço': pesq_values['-VAL-PRC-']
                }

                try:
                    self.app.atualiza_produto( produto )
                    self.limpar()
                    self.pesquisa( pesq_values )
                except Exception as err:
                    self.window['-ERR-ATT-']( 'Erro: ' + str(err) )

            elif pesq_event == '-ADICIONAR-':
                adc = JanelaAdicao( self.app )
                if adc.modificado:
                    self.pesquisa( pesq_values )

    def pesquisa( self, values ):
        ordenacao = list( filter( lambda key: values[key], values ) )[0] # Desculpa
        self.app.busca_produtos( ordenacao, self.window )

    def limpar( self ):
        self.codigo_selecionado = None
        elementos = [ '-ERR-ATT-', '-TXT-COD-', '-VAL-NOME-', '-VAL-PRC-' ]
        for elemento in elementos:
            self.window[elemento]('')

    def fechar( self ):
        self.window.close()
