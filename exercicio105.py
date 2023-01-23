'''Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A média da turma
- A situação (opcional)'''

def notas(num, sit=False):
    """
    -> Função que mostra uma situação geral de notas dos alunos:
    :param qtdnt: quantidade de notas inseridas;
    :param maiorn: maior nota inserida;
    :param menorn: menor nota inserida;
    :param median: média das notas inseridas;
    :param sit: situação dos alunos;
    :return: retorna todos os parametros acima dentro ou não de uma situação
    """
    dictnt = dict()
    dictnt['total'] = len(num)
    dictnt['maior'] = max(num)
    dictnt['menor'] = min(num)
    dictnt['média'] = sum(num)/len(num)
    print(type(num))
    if sit:
        if dictnt['média'] >= 9:
            dictnt['sit'] = 'ÓTIMA'
        elif dictnt['média'] >= 7:
            dictnt['sit'] = 'BOA'
        elif dictnt['média'] >= 5:
            dictnt['sit'] = 'REGULAR'
        else:
            dictnt['sit'] = 'RUIM'
    return dictnt

