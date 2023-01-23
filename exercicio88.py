'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre
1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import choice
from time import sleep
print(f'{"MEGA SENA":=^60}')
all = []
palpite = []
for c in range(1,61) :
    all.append(c)
while True :
    qjogos = int(input("Quantos palpite deseja ver : "))
    for j in range(1,qjogos + 1):
        for c in range(1,7):
            palpite.append(choice(all))
        print(f'jogo {j} : {palpite}')
        palpite.clear()
        sleep(1)
    conf = str(input("Quer continuar [S/N] : ")).strip()[0]
    while conf not in "SsNn" :
        conf = str(input("Tente Novamente!! .Continuar [S/N] : ")).strip()[0]
    print("-=" * 30)
    if conf in "Nn" :
        break