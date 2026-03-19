from time import sleep
import os
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
        titulo_centralizado = Align.center("[bold green]GERADOR DE SENHA[/bold green]")
        console.print(Panel(titulo_centralizado,expand=True, border_style="green", ))
        self.indices = [1, 2, 3, 4, 5]

    def quantidade_caracs(self):
        while True:
            personalizado = False
            Util.limpar_tela()
            self.__init__()
            print(f'\n{"TAMANHO DA SENHA":^70}\n')
            print('=' * 70)
            print('[1] 4 Dígitos              [2] 6 Dígitos')
            print('[3] 8 Dígitos              [4] 12 Dígitos')
            print('[5] Tamanho Personalizado')
            print('-' * 70)
            try:
                quantidade_carac = int(input('Informe a opção desejada: '))
                if quantidade_carac not in [1, 2, 3, 4, 5]:
                    print('ERRO! INFORME UMA OPÇÃO VÁLIDA')
                    sleep(2)
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
            except:
                print('ERRO! INSIRA UM NÚMERO!')
                sleep(1)
            if personalizado:
                try:
                    quantidade_carac = int(input('Informe a quantidade de caracteres que a senha terá: '))
                    if quantidade_carac < 4:
                        print('\nSenha muito pequena! O tamanho mínimo de senha é 4 caracteres')
                        sleep(2)
                    elif quantidade_carac > 100:
                        print('\nSenha muito grande! O tamanho máximo de senha é 100 caracteres')
                        sleep(2)
                    else:
                        return quantidade_carac
                except:
                    print('ERRO! INSIRA UM NÚMERO!')
                    sleep(1)
                    Util.limpar_tela()
                    self.__init__()

    def preferencias(self, lista_verificado=None):
        Util.limpar_tela()
        for i, valor in enumerate(self.indices):
            for j in lista_verificado:
                if valor == j:
                    self.indices[i] = '\u2714'
        print('=' * 70)
        print(f'{"POSSÍVEIS CARACTERES DA SENHA":^70}')
        print('=' * 70)
        print(f'[{self.indices[0]}] Caracteres Especiais (!, @, #, $, %, &, *, -, _, +, =, /, ?, .)')
        print(f'[{self.indices[1]}] Letras Maiúscula          [{self.indices[2]}] Letras Minúsculas')
        print(f'[{self.indices[3]}] Números                   [{self.indices[4]}] Todas as opções')
        print(f'[6] Gerar Senha               [7] Voltar')
        print('-' * 70)

'''
PAINEL COM O TÍTULO "GERADOR DE SENHAS CRIADO". PRÓXIMO PASSO É DESENVOLVER TABELAS, OUTROS PAINÉIS OU O QUE FOR
INTERESSANTE APLICAR NO MENU QUE SELECIONA A QUANTIDADE DE DÍGITOS E O MENU DOS TIPOS DE CARACTERES. PENSO EM DEIXAR
TUDO NA COR VERDE. PRA CONTRASTAR UM POUCO COM O TERMINAL E FICA NA VIBE ESTERIOTIPADA DE HACKER COM TEMA VERDE E PRETO.
PRA SAÍDA, É BOM COLOCAR ALGUMA OUTRA COR MAIS DESTACADA. TALVEZ UM bold yellow, OU bold purple.
'''