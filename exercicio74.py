''' Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. '''

from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')