'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas
posições na lista.'''

pos_menor = list()
pos_maior = list()
from random import randint as rd

lista = [rd(0, 9), rd(0, 9), rd(0, 9), rd(0, 9), rd(0, 9), ]
for c in range(0, len(lista)):
    if min(lista) == lista[c]:
        pos_menor.append(c)
    if max(lista) == lista[c]:
        pos_maior.append(c)

print(lista)
print(
    f'O menor número da lista é [ {min(lista)} ] ele aparece {lista.count(min(lista))} vezes, na posição {pos_menor}.')
print(
    f'O maior número da lista é [ {max(lista)} ] ele aparece {lista.count(max(lista))} vezes, na posição {pos_maior}.')