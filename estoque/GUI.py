import PySimpleGUI as sg
from main import *


produtos_: list = load_pkl()
setores: tuple = ('alimentos', 'higiene', 'brinquedos', 'bebidas', 'outros')


def janela_menu():
    buttons = [[sg.B("Ver estoque")],
               [sg.B("Cadastrar produto")],
               [sg.B("Remover produto")],
               [sg.B("Pesquisar produto")],
               [sg.B("Salvar")],
               [sg.B("Exit")]]

    # layout = [[sg.Frame("", layout=buttons)]]
    return sg.Window("Menu", layout=buttons, finalize=True)


def janela_estoque():

    i = 1
    for produto in produtos_:
        produto.atualizar_id(i)
        i += 1

    headings = ['ID', 'Nome', 'Preço(R$)', 'Setor']
    produtos_info = []
    for produto in produtos_:
        produtos_info.append([produto.id, produto.nome.title(), f"{produto.valor:.2f}", produto.setor])

    layout = [[sg.Table(values=produtos_info, headings=headings, auto_size_columns=True)],
              [sg.B("Voltar")]]
    return sg.Window("Estoque", layout=layout, finalize=True)


def janela_cadastro():
    layout = [[sg.Text("Nome do produto:"), sg.I("", key="-NAME-")],
              [sg.Text("Valor do produto:"), sg.I("", key="-PRECO-")],
              [sg.Text("Setor do produto:"), sg.Combo(setores, key="-SETOR-")],
              [sg.Text("", key="-OUT-", justification='center')],
              [sg.B("Voltar"), sg.B("Submit")]]
    return sg.Window("Cadastro", layout=layout, finalize=True)


def janela_remover():

    nome_produtos = [f"{produto.nome} -- R$ {produto.valor:.2f} -- {produto.setor}"
                     for produto in produtos_]

    layout = [[sg.Text("Escolha um produto para remover:"),
               sg.Combo(nome_produtos, key="-REMOV-", size=35)],
              [sg.Text("", key="-OUT-")],
              [sg.B("Voltar"), sg.B("Apply")]]
    return sg.Window("Remover", layout=layout, finalize=True)


janela1, janela2 = janela_menu(), None

while True:
    window, event, values = sg.read_all_windows()
    print(f"{event}; {values}")

    if window == janela1:
        janela2 = None

        # fechar programa
        if event == "Exit" or event == sg.WINDOW_CLOSED:
            break
        # ver estoque
        elif event == "Ver estoque":
            janela1.hide()
            janela2 = janela_estoque()
        # cadastro
        elif event == "Cadastrar produto":
            janela1.hide()
            janela2 = janela_cadastro()
        # remover
        elif event == "Remover produto":
            janela1.hide()
            janela2 = janela_remover()
        # salvar
        elif event == "Salvar":
            salvar(produtos_)
            sg.popup("Modificaçoes salvas com êxito.")

    elif window == janela2:
        # voltar para menu
        if event == "Voltar" or event == sg.WIN_CLOSED:
            janela2.hide()
            janela1.un_hide()
        # enviar
        elif event == "Submit":
            novo_produto = Produto(values["-NAME-"], float(values["-PRECO-"]), values["-SETOR-"])
            produtos_.append(novo_produto)
            janela2["-OUT-"].update("Produto adicionado!")
        # remover
        elif event == "Apply":
            i = 0
            for produto in produtos_.copy():
                if produto.nome in values["-REMOV-"]:
                    del produtos_[i]
                i += 1
            janela2["-OUT-"].update("Produto removido!")


window.close()
