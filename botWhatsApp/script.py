#Abrir o whatsapp no computador quando o envio inicar.
#Validar os campos em branco antes de executar qualquer função.
#Fazer um login na entrada  da aplicação 
#Adicionar opções de deletar com
#Alterar o staus de envio na base de dados
#Capturar caminho do video pelo input Browse
#Criar um módulo que valida os telefones.
#Criar módulo de instalação: Criador do banco de dados. Instalação do whatsapp.

import sys
sys.path.append('modulos')

import disparoMensagens
import baseContatos
from PySimpleGUI import PySimpleGUI as sg

dbContatos = baseContatos.ContactDataBase()
# sg.theme_previewer()
#Layout
sg.theme('Reddit')
layout = [
    
    [sg.Text('\tBEM VINDO AO ROBÔ DE WHATSAPP \n\n',font='Courier 15', text_color='Black')],
    [sg.Text('Contatos:',font='Courier 12', text_color='Black')],
    [sg.Text('Listar contatos:'),sg.Text('\t'),sg.Button('Listar contatos')],
    [sg.Text('Buscar Contato:'),sg.Text('\t'),sg.Input(key='buscar contato',size=(20,0)),sg.Button('Buscar')],
    [sg.Text('Inserir Contato:'),sg.Text('\t '),sg.Input(key='inserir contato',size=(20,0)),sg.Button('Inserir')],
    [sg.Text('Inserir Contatos em lote:'),sg.Text('  '),sg.Input(key='pesquisar arquivo',size=(20,0)), sg.FileBrowse(),sg.Button('Carregar')],
    [sg.Text('\n\n')],
    [sg.Text('Mensagem:',font='Courier 12', text_color='Black')],
    [sg.Text('Inserir texto da mensagem:'),sg.InputText(key='-MENSAGEM-',size=(50,20))],
    [sg.Text('Inserir Imagem:'),sg.Input(key='-IMGEM-',size=(20,0)), sg.FileBrowse(),sg.Button('Carregar')],
    [sg.Text('Inserir Video:'),sg.Input(key='-VIDEO-',size=(20,0)), sg.FileBrowse(),sg.Button('Carregar')],
    [sg.Text('\n\n')],
    [sg.Text('Enviar Mensagem ou mensagem com imagem'), sg.Button('Enviar Mensagem',size=(15, 1),button_color=('green'))],
    [sg.Text('Enviar Mensagem ou mensagem com video'), sg.Button('Enviar Video',size=(15, 1),button_color=('green'))],
    [sg.Text('Apagar base:'),sg.Button('Apagar',button_color=('red'))],
    [sg.Text('\n\n')],
    [sg.Button('Sair',size=(7, 1),button_color=('red'))],
    [sg.Text('\n\n')],
]

#Janela
janela = sg.Window('WhatsappBot',layout,size=(1000,800))

#Ler eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    elif eventos == 'Listar contatos':
        celular = dbContatos.readContacts()
        sg.popup_scrolled(celular,size=(35,15), title='Lista de contatos:')
    elif eventos == 'Buscar':
        celular = dbContatos.readContact(valores['buscar contato'])
        janela['buscar contato'].update('')
        sg.popup_scrolled(celular,size=(35,15), title='Buscar Contato')    
    elif eventos == 'Inserir':
        inserir = dbContatos.insertContact(valores['inserir contato'])
        janela['inserir contato'].update('')
        sg.Popup(inserir)
    elif eventos == 'Carregar':
        inserirLote = dbContatos.insertContacts(valores['pesquisar arquivo'])
        janela['pesquisar arquivo'].update('')
        sg.Popup(inserirLote)
    elif eventos == 'Enviar Mensagem':
        contatos = dbContatos.readContacts()
        bot = disparoMensagens.WhatsappBot()
        mensagem = valores['-MENSAGEM-']
        imagem = valores['-IMGEM-']
        finalizacao = bot.EnviarMensagens(contatos,mensagem,imagem)
        janela['-IMGEM-'].update('')
        sg.Popup('MENSAGENS ENVIADAS COM SUCESSO!!!')
    elif eventos == 'Enviar Video':
        contatos = dbContatos.readContacts()
        bot = disparoMensagens.WhatsappBot()
        mensagem = valores['-MENSAGEM-']
        video = 'C:\\Users\\f48014593820\\Videos\\BotWhatsapp.mp4' #Fazer a alteração disso
        finalizacao = bot.EnviarVideo(contatos,mensagem,video)
        janela['-VIDEO-'].update('')
        sg.Popup('MENSAGENS ENVIADAS COM SUCESSO!!!')
    elif eventos == 'Apagar':
        finalizacao = dbContatos.limparBase()
        sg.Popup(finalizacao)
    elif eventos == 'Sair':
        janela.close()

    janela.Refresh()