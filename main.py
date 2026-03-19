import random
from time import sleep
from design_cli import Tela, Util

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