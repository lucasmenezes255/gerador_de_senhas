from rich import print as rprint

class Error():
    def __init__(self):
        pass

    @staticmethod
    def insirer_opcao_valida():
        """
        :return: Retorna uma mensagem de erro para caso a opção inserida não seja uma que o programa reconheça
        """
        rprint('\n[b u red1]ERRO! INSIRA UMA OPÇÃO VÁLIDA![/]')

    @staticmethod
    def nenhuma_opcao_selecionada():
        """
        :return: Mensagem de erro especial para caso seja inserida a opção de gerar senha, mas a lista de possíveis
        caracteres esteja vazia
        """
        rprint('\n[b u red1]ERRO! NENHUNHA OPÇÃO SELECIONADA. ESCOLHA PELO MENOS 1 OPÇÃO[/]')

