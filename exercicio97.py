'''Faça um programa que tenha uma função chamada escreva(), que receba um texto
qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.'''

def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print('  {msg}')
    print('~' * tam)
escreva('Vinicius Trindade')
escreva('Curso de Python no Youtube')
escreva('CeV')