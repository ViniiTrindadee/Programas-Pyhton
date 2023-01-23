'''Faça um mini-sistema que utilize o Interactive Help do Python. O usuário
vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra
‘FIM’, o programa se encerrará. Importante: use cores.'''

def pyhelp():
    from time import sleep
    while True:
        print('\033[1;97;42m~' * 30)
        print(f'{"SISTEMA DE AJUDA PyHELP":^30}')
        print('~' * 30)

        resp = input('\033[mFunção ou Biblioteca: ').lower()
        while resp == '':
            print('\033[1;30;41m~' * 32)
            print(f'{"Nenhum comando foi digitado!":^32}')
            print('~' * 32)
            resp = input('\033[mFunção ou Biblioteca: ').lower()
        if resp == 'fim':
            break

        tam = len(resp)
        print('\033[1;97;46m~' * (tam + 36))
        print(f"  Acessando o manual do comando '{resp}'")
        print('~' * (tam + 36))
        print('\033[0;30;107m', end='')
        sleep(1)
        help(resp)
        sleep(2)

    print('\033[1;97;45m~' * 13)
    print(f'{"ATÉ LOGO!":^13}')
    print('~' * 13)
    sleep(1)


# Programa Principal
pyhelp()