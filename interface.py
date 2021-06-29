import PySimpleGUI as sg

sg.theme( 'LightGreen3' )

window = sg.Window( 'Terminal', layout=[
    # Cabeçalhp
    [ sg.Text( '', size=( 32, None ), key='-TXT-CAB-' ) ],

    # Lista de compras
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
        sg.Button( 'Adicionar', key='-BTN-ADC-' ),
        sg.Button( 'Pesquisar produtos', key='-BTN-PESQ-' )
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
    [ sg.Button( 'Finalizar', key='-BTN-FIN-' ) ],
    
    # Sair
    [ sg.Button( 'Sair', button_color='red', key='-BTN-SAIR-' ) ]
])

def limpa_terminal():

    keys = [
        '-TXT-TOTAL-', '-TXT-TROCO-',
        '-COD-ADC-', '-QTD-ADC-', '-ERR-ADC-',
        '-COD-REM-', '-QTD-REM-', '-ERR-REM-',
        '-VAL-PGTO-', '-SUC-PGTO-', '-ERR-PGTO-'
    ]

    window['-COMPRAS-'].update([])

    for key in keys:
        window[key]('')

def cria_janela_pesquisa():
    return sg.Window( 'Pesquisa', layout=[
        [ sg.Text( 'Ordenar por:' )],
        [
            sg.Radio( 'Código', 'ORDENACOES', True, key='1' ),
            sg.Radio( 'Nome', 'ORDENACOES', key='2' ),
            sg.Radio( 'Preço', 'ORDENACOES', key='3' )
        ],
        [ sg.Button( 'Pesquisar', key='-BTN-PESQ-' ) ],
        [ sg.Text( 'Produtos:' ) ],
        [ sg.Listbox([], size=(32, 10), key='-PRODUTOS-') ],
        [ sg.Button( 'Sair', button_color='red', key='-BTN-SAIR-' ) ]
    ])