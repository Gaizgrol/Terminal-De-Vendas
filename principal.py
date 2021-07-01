from aplicacao import Aplicacao
from janela_principal import JanelaPrincipal
import PySimpleGUI as sg
import locale

# Localização
locale.setlocale( locale.LC_TIME, "pt_BR" )

# Controle lógico
app = Aplicacao()
# Interface
sg.theme( 'LightGreen3' )
JanelaPrincipal( app )

print( "Até logo :)" )
