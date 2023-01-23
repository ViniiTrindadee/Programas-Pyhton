import random

computador = ['PEDRA', 'PAPEL', 'TESOURA']
sort = random.choice(computador)

print('\033[0;33m-=\033[m' * 10)
print('Vamos jogar Jokenpo!')
print('\033[0;33m-=\033[m' * 10)
Usuario = str(input('PEDRA\n'
                    'PAPEL\n'
                    'TESOURA\n'
                    'Qual você quer? ')).strip().upper()

print('\033[0;33m-=\033[m' * 10)

if Usuario != 'PEDRA' and Usuario != 'PAPEL' and Usuario != 'TESOURA':
    print('NÃO VALE!')

if Usuario == 'PEDRA' and sort == 'PEDRA':
    print('PEDRA COM PEDRA! Empatou!')
elif Usuario == 'PEDRA' and sort == 'PAPEL':
    print('PEDRA COM PAPEL! VOCÊ PERDEU :)')
elif Usuario == 'PEDRA' and sort == 'TESOURA':
    print('PEDRA COM TESOURA! VOCÊ GANHOU :(')

if Usuario == 'PAPEL' and sort == 'PAPEL':
    print('PAPEL COM PAPEL! Empatou!')
elif Usuario == 'PAPEL' and sort == 'PEDRA':
    print('PAPEL COM PEDRA! VOCÊ GANHOU :(')
elif Usuario == 'PAPEL' and sort == 'TESOURA':
    print('PAPEL COM TESOURA! VOCÊ PERDEU :)')

if Usuario == 'TESOURA' and sort == 'TESOURA':
    print('TESOURA COM TESOURA! Empatou!')
elif Usuario == 'TESOURA' and sort == 'PEDRA':
    print('TESOURA COM PEDRA! VOCÊ PERDEU :)')
elif Usuario == 'TESOURA' and sort == 'PAPEL':
    print('TESOURA COM PAPEL! VOCÊ GANHOU :(')

print('\033[0;33m-=\033[m' * 10)