from rich import print as rprint
from time import sleep

class Error():
    def __init__(self):
        pass

    @staticmethod
    def insirer_opcao_valida():
        """
        :return: Retorna uma mensagem de erro para caso a opção inserida não seja uma que o programa reconheça
        """
        rprint('\n[b u red1]ERROR_001: INSIRA UMA OPÇÃO VÁLIDA![/]')
        sleep(2)

    @staticmethod
    def nenhuma_opcao_selecionada():
        """
        :return: Mensagem de erro especial para caso seja inserida a opção de gerar senha, mas a lista de possíveis
        caracteres esteja vazia
        """
        rprint('\n[b u red1]ERROR_002: NENHUNHA OPÇÃO SELECIONADA. ESCOLHA PELO MENOS 1 OPÇÃO[/]')
        sleep(1.5)


