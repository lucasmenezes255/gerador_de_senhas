import random
from time import sleep
from design_cli import Tela, Util
from rich.console import Console
from pyperclip import copy
from erros import Error

console = Console()
class Senha:
    def __init__(self):
        self.alfabeto_lowcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.alfabeto_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.caracs_especiais = ['!', '@', '#', '$', '%', '&', '*', '-', '_', '+', '=', '/', '?', '.']
        self.caracs_senha = []

    def selecao_caracteres(self, lista_escolhas):
        """
        Configura o conjunto de caracteres que a senha terá

        Recebe uma lista com números de 1 a 5 que indicam quais tipos de caracteres a senha possuirá
        """
        lista_escolhas_unica = set(lista_escolhas)
        caracteres_finais = set()
        mapa_caracteres = {1: self.caracs_especiais, 2: self.alfabeto_uppercase,
                           3: self.alfabeto_lowcase, 4: self.numeros}

        for opcao in lista_escolhas_unica:
            if opcao == 5:
                caracteres_finais.update(self.caracs_especiais, self.alfabeto_uppercase,
                                               self.alfabeto_lowcase, self.numeros)
            else:
                caracteres_finais.update(mapa_caracteres[opcao])

        self.caracs_senha = list(caracteres_finais)

    def gerar_senha(self, tamanho_senha):
        """
        Gera uma string aleatória definida pelo tamanho da senha e seus possíveis caracteres

        :param tamanho_senha: Recebe um número que define o tamanho da string da senha
        :return: Retorna a string da senha já limitada pelo tamanho e pelos possíveis caracteres que pode possuir
        """
        senha = ''.join(random.choices(self.caracs_senha, k=tamanho_senha))
        return senha

escolha_preferencias = None
lista_escolha = []
criacao_senha = Senha()
tela_senha = Tela()
quantidade_caracteres = tela_senha.quantidade_caracs()
if quantidade_caracteres != 6:
    while True:
        Util.limpar_tela()
        tela_senha.preferencias(lista_escolha)
        try:
            escolha_preferencias = int(console.input('\n[cyan1]Escolha uma opção[/] '
                                                     '[u bright_magenta](em caso de várias escolha, selecione 1 por vez):[/] '))
            if escolha_preferencias not in [1, 2, 3, 4, 5, 6, 7]:
                Error.insirer_opcao_valida()
            else:
                if escolha_preferencias != 6:
                    if escolha_preferencias == 5:
                        lista_escolha = [5]
                        break
                    elif escolha_preferencias == 7:
                        lista_escolha = []
                        tela_senha.quantidade_caracs()
                    else:
                        lista_escolha.append(escolha_preferencias)
                else:
                    if lista_escolha == []:
                        Error.nenhuma_opcao_selecionada()
                    else:
                        break
            sleep(0.5)
        except:
            Error.insirer_opcao_valida()
    criacao_senha.selecao_caracteres(lista_escolha)
    senha_gerada = criacao_senha.gerar_senha(quantidade_caracteres)

    console.print(f'\n[green_yellow]SENHA GERADA:[/] [b u green_yellow]{senha_gerada}[/]')
    console.print('\n[dim pale_turquoise1]Copiado para a área de transferência![/]')
    copy(senha_gerada)
else:
    console.print('\n[red3]Saindo...[/]')
    sleep(1.75)
