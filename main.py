import random
from time import sleep
import os


class Util:
    def __init__(self):
        pass

    @staticmethod
    def limpar_tela():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')


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
        lista_escolhas_unica = set(lista_escolhas)
        for i in lista_escolhas_unica:
            if i == 1:
                self.caracs_senha = self.caracs_senha + self.caracs_especiais
            elif i == 2:
                self.caracs_senha = self.caracs_senha + self.alfabeto_uppercase
            elif i == 3:
                self.caracs_senha = self.caracs_senha + self.alfabeto_lowcase
            elif i == 4:
                self.caracs_senha = self.caracs_senha + self.numeros
            elif i == 5:
                self.caracs_senha = (self.caracs_especiais + self.alfabeto_uppercase + self.alfabeto_lowcase +
                                     self.numeros)

    def gerar_senha(self, tamanho_senha):
        senha = ''.join(random.choices(self.caracs_senha, k=tamanho_senha))
        return senha


class Tela:
    def __init__(self):
        print('=' * 70)
        print(f'{"GERADOR DE SENHA":^70}')
        print('-' * 70)
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


escolha_preferencias = None
lista_escolha = []
criacao_senha = Senha()
tela_senha = Tela()
quantidade_caracteres = tela_senha.quantidade_caracs()
while True:
    Util.limpar_tela()
    tela_senha.preferencias(lista_escolha)
    try:
        escolha_preferencias = int(input('Escolha uma opção (em caso de várias escolha, selecione 1 por vez): '))
        if escolha_preferencias not in [1, 2, 3, 4, 5, 6, 7]:
            print('\nERRO! INSIRA UM NÚMERO VÁLIDO')
            sleep(1)
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
                    print('ERRO! Nenhuma opção selecionada. Selecione pelo menos 1 opção')
                    sleep(1.5)
                else:
                    break
        sleep(0.5)
    except:
        print('\nERRO! INSIRA UM NÚMERO!')
        sleep(1)
criacao_senha.selecao_caracteres(lista_escolha)
senha_gerada = criacao_senha.gerar_senha(quantidade_caracteres)

print('=' * 70)
print(f'\nSENHA GERADA: {senha_gerada}')

'''
CRIEI UMA TELA NO TERMINAL COM ESCOLHAS PREDEFINIDAS DE SENHAS E POSSIBILIDADE DE PERSONALIZAR O TAMANHO DA SENHA
PORÉM AINDA É NECESSÁRIO MAIS REFINO:
- COLOCAR UM NÚMERO MINÍMO DE TAMANHO PRA SENHA. TAMANHO MÍNIMO SÃO 4 CARACTERES. --- FEITO

- O SISTEMA DE SELECIONAR OS CARACTERES POSSÍVEIS DA SENHA TÁ LEGAL, TRATADO MAS FALTA ALGO QUE QUERO IMPLEMENTAR:
  TODA VEZ QUE O USUÁRIO SELECIONAR UMA OPÇÃO DE CARACTER, ANTES DE GERAR A SENHA O NÚMERO DA OPÇÃO ESCOLHIDA SE TORNA 
  UM 'V' DE CONFIRMADO. ASSIM ELE VÊ AS OPÇÕES ESCOLHIDAS - FEITO

- IMPLEMENTAR A FINALIZAÇÃO DO FLUXO QUANDO SELECIONA '6' NOS CARACTERES E NÃO POSSUI NENHUM NÚMERO SELECIONADO. 
IMPLEMENTAR PRA SÓ SER POSSÍVEL GERAR SENHA QUANDO A LISTA DE POSSIBILIDADES DE CARACTERES NÃO ESTIVER VAZIA - FEITO

- IMPLEMENTAR AGORA A RELAÇÃO ENTRE A QUANTIDADE DE CARACTERES ESCOLHIDA E AS POSSIBILIDADES DE CARACTERES. ISSO COM O
  random.choices(). COLOCA COMO PARÂMETROS A LISTA E A QUANTIDADE SELECIONADA PODENDO REPETIR.  random.choices(lista, k=n) - FEITO
'''