import pickle
import os

from rich import print
from rich.table import Table
from rich.panel import Panel
from rich.console import Console


class Produto:
    def __init__(self, nome: str, valor: float, setor: str):
        self.nome = nome.title()
        self.id = 000
        self.valor = valor
        self.setor = setor

    def show_info(self):
        print(f'Nome: {self.nome}; Valor: R${self.valor}; Setor: {self.setor}')

    def atualizar_valor(self, novo_valor):
        self.valor = novo_valor

    def atualizar_id(self, novo_id):
        self.id = "{:003}".format(novo_id)


def limpar_tela():
    if os.name == 'ntf':
        os.system('clc')
    else:
        os.system('clear')


def load_pkl():
    global produtos
    if os.path.isfile('arquivo.pkl'):
        with open('arquivo.pkl', 'rb') as arquivo_load:
            produtos = pickle.load(arquivo_load)
            return produtos

def menu():
    limpar_tela()
    compl = "\n--+-----------------------"
    texto = f"""
-1| sair{compl}
 0| exibir todo estoque{compl}
 1| cadastrar produto{compl}
 2| remover produto{compl}
 3| pesquisar produto{compl}
 4| salvar
"""
    print(Panel.fit(texto, title='MENU'))


def imprimir_estoque():
    tabela = Table(title='ESTOQUE')

    tabela.add_column("Produto")
    tabela.add_column("ID")
    tabela.add_column("Preço(R$)", justify='right')
    tabela.add_column("Setor")

    i = 1
    for produto in produtos:
        produto.atualizar_id(i)
        i += 1
        tabela.add_row(str(produto.nome), produto.id, f'{produto.valor:.2f}', str(produto.setor))

    console = Console()
    console.print(tabela)
    input("Enter p/ sair\n")


def cadastro_produto():
    nome = input('digite o nome do produto: ')
    valor = float(input('digite o valor em reais do produto: R$ '))
    setor = input('digite o setor do produto: ')

    produto = Produto(nome, valor, setor)
    produtos.append(produto)
    print('Produto cadastrado!')
    input("Enter p/ sair\n")


def remover_produto():
    busca = input('digite o nome do produto para remover: ')
    i = 0
    for produto in produtos:
        if busca == produto.nome:
            del produtos[i]
        i += 1
    print('Produto removido!')
    input("Enter p/ sair\n")


def pesquisar():
    busca = input('digite o nome do produto para pesquisar: ')
    achou = False
    for produto in produtos:
        if busca in produto.nome:
            produto.show_info()
            achou = True

    if not achou:
        print('produto nao encontrado')
    input("Enter p/ sair\n")


def salvar(file):
    with open('arquivo.pkl', 'wb') as arquivo_dump:
        pickle.dump(file, arquivo_dump)
    print('Salvo!')


produtos = load_pkl()
def main():
    while True:
        menu()
        op = int(input('opcao: '))
        limpar_tela()

        match op:
            case -1:
                break
            case 0:
                imprimir_estoque()
            case 1:
                cadastro_produto()
            case 2:
                remover_produto()
            case 3:
                pesquisar()
            case 4:
                salvar(produtos)
            case _:
                print('opcao invalida')


if __name__ == '__main__':
    main()
