''' Crie um programa que tenha a função leiaInt(), que vai funcionar de
forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar
apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''

def leiaInt(a: str):
    while True:
        valor = input(a)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mERRO! Digite um número válido\033[m')


n = leiaInt('Digite um valor: ')
print(f'Você acabou de digitar o número {n}')