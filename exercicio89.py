'''Crie um programa que leia nome e duas notas de vários alunos e guarde
tudo em uma lista composta. No final, mostre um boletim contendo a média de cada
um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = []
notas = []
media = []
while True:
    alunos.append(str(input('Nome: ')))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2:'))
    n3 = [n1, n2]
    m = (n1 + n2) / 2
    media.append(m)
    notas.append(n3)

    con = str(input('Adicionar mais alunos s/n? ')).strip()
    if con in 'Nn':
        break

print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-'*30)
for x in range(0, len(alunos)):
    print(f'{x:<4}{alunos[x]:<10}{media[x]:>8.1f}')
print('-'*30)
while True:
    alunox = int(input('Mostrar a nota de qual aluno? (999 para fechar)'))
    print(f'as notas de {alunos[alunox]} são: {notas[alunox]}')
    print('-' * 50)
    if alunox == 999:
        break
print('PROGRAMA FINALIZADO!')