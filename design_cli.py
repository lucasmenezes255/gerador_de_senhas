from time import sleep
import os
from erros import Error
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich import print as rprint
console = Console()

class Util:
    def __init__(self):
        pass

    @staticmethod
    def limpar_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

class Tela:
    def __init__(self):
        titulo_centralizado = Align.center("[bold green1]GERADOR DE SENHA[/bold green1]")
        console.print(Panel(titulo_centralizado,expand=True, border_style="green1", ))
        self.indices = [1, 2, 3, 4, 5]

    def quantidade_caracs(self):
        """
        :return: Menu de seleção do tamanho da senha
        """
        while True:
            Util.limpar_tela()
            self.__init__()
            tabela = Table(title="[green bold]TAMANHO DA SENHA[/]", show_header=False, box=box.ASCII)
            tabela.add_column("num1", style="green1 bold", justify="right")
            tabela.add_column("desc1", style="white bold")
            tabela.add_column("num2", style="green1 bold", justify="right")
            tabela.add_column("desc2", style="white bold")

            tabela.add_row("1", "4 Dígitos", "2", "6 Dígitos")
            tabela.add_row("3", "8 Dígitos", "4", "12 Dígitos")
            tabela.add_row("5", "Tamanho Personalizado", "6", "Sair")
            console.print(tabela)

            personalizado = False
            try:
                quantidade_carac = int(console.input('[i bright_magenta]Informe a opção desejada: [/]'))
                if quantidade_carac not in [1, 2, 3, 4, 5, 6]:
                    Error.insirer_opcao_valida()
                elif quantidade_carac == 1:
                    quantidade_carac = 4
                    return quantidade_carac
                elif quantidade_carac == 2:
                    quantidade_carac = 6
                    return quantidade_carac
                elif quantidade_carac == 3:
                    quantidade_carac = 8
                    return quantidade_carac
                elif quantidade_carac == 4:
                    quantidade_carac = 12
                    return quantidade_carac
                elif quantidade_carac == 5:
                    personalizado = True
                elif quantidade_carac == 6:
                    return 6
            except:
                Error.insirer_opcao_valida()
            if personalizado:
                try:
                    quantidade_carac = int(console.input('[i blue1]Informe a quantidade de caracteres que a senha terá: [/]'))
                    if quantidade_carac < 4:
                        rprint('\n[b u red1]SENHA MUITO PEQUENA! O TAMANHO MÍNIMO É 4 CARACS[/]')
                        sleep(2)
                    elif quantidade_carac > 100:
                        rprint('\n[b u red1]SENHA MUITO GRANDE! O TAMANHO MÁXIMO É 100 CARACS[/]')
                        sleep(2)
                    else:
                        return quantidade_carac
                except:
                    Error.insirer_opcao_valida()
                    Util.limpar_tela()
                    self.__init__()

    def preferencias(self, lista_verificado=None):
        """
        Menu de seleção dos possíveis caracteres que a senha pode ter. Após selecionar uma opção, seu índice
         é substituído por um ícone de 'CHECK'

         :param lista_verificado: Recebe as opções escolhidas pelo menu para substituir elas pelo 'CHECK' na tela
        """
        Util.limpar_tela()
        for i, valor in enumerate(self.indices):
            for j in lista_verificado:
                if valor == j:
                    self.indices[i] = '[green1]\u2714[/]'
        titulo_centralizado = Align.center("[b green1]POSSÍVEIS CARACTERES DA SENHA[/]")
        rprint((Panel(titulo_centralizado, expand=True, border_style="green1")))
        tabela = Table(title="", show_header=False, box=None)

        tabela.add_column(header="num1", style="turquoise2 bold")
        tabela.add_column(header="desc1", style="medium_orchid1 bold")
        tabela.add_column(header="num2", style="turquoise2 bold")
        tabela.add_column(header="desc2", style="medium_orchid1 bold")

        tabela.add_row(str(self.indices[0]),
                       "Caracteres Especiais [light_goldenrod1 bold](!, @, #, $, %, &, *, -, _, +, =, /, ?, .)[/]",
                       "", "")
        tabela.add_row(str(self.indices[1]), "Letras Maiúscula", str(self.indices[2]), "Letras Minúsculas")
        tabela.add_row(str(self.indices[3]), "Números", str(self.indices[4]), "Todas as opções")
        tabela.add_row("6", "Gerar Senha", "7", "Voltar")
        tabela.add_row("","[not bold khaki1]A opção [/][not bold u khaki1]5[/]"
                          "[not bold khaki1] marca todas as outras opções de caracteres "
                       "e gera a senha [red1]AUTOMATICAMENTE[/]",
                       "", "")
        console.print(tabela)