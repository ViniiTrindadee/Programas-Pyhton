'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = 0
for l in range(0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para posição [{l}, {c}]: '))
        if lista[l][c] % 2 == 0:
            par += lista[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print('')
print(f'A soma dos valores pares é: {par}')
print(f'A soma dos valores da terceira coluna é: {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O maior valor da segunda linha é: {max(lista[1])}')