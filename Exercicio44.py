# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros


print('=-=-=-=-=-' * 7)
preco = float(input('Preço das compras:  '))
print('''Formas de pagamento:
[ 1 ] à vista em dinheiro
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opc = int(input('Qual é sua opção:  '))
if opc == 1:
    print('Sua compra de R${:.2f} vai custar {:.2f} com 10% de desconto'.format(preco, 90 / 100 * preco))
elif opc == 2:
    print('Sua compra de R${:.2f} no cartão vai custar {:.2f} com 5% de desconto'.format(preco, 95 / 100 * preco))
elif opc == 3:
    print('''Sua compra será parcelada em 2x de R${:.2f} sem juros
O total será de R${:.2f}'''.format(preco / 2, preco))
elif opc == 4:
    parcelas = int(input('Quantas parcelas?'))
    if parcelas < 3:
        print('''Nùmero de parcelas invalido, por favor digite 3 ou maior:''')
    elif parcelas >= 3:
        juros = 20 / 100 * preco
        parcela = (preco / parcelas) + (juros / parcelas)
        print('''Sua compra será parcelada em {}x de R${:.2f} COM JUROS
Sua compra de R${:.2f} vai custar R${:.2f} no final.'''.format(parcelas,parcela, preco,preco + juros))
else:
    print('Forma de pagamento invalida, por favor digite novamente:')
