'''Crie um programa que tenha uma função chamada voto() que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando
se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f'Direito de voto aos {idade} anos "NEGADO"!'
    elif idade >= 65:
        return f'Direiro de voto aos {idade} anos "OPCIONAL"!'
    else:
        return f'Direito de voto aos {idade} anos "OBRIGATÓRIO"!'


# ============================================================================================| Main Program
ano = int(input('Ano de nascimento: '))
print('-' * 40)
n1 = voto(ano)
print(n1)