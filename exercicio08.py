salário = float(input("Qual é o salário do funcionario?R$: "))
novo = salário +(salário*15/100)
print('Um funcionario que ganhava R$ {}, com 15% de aumento, passa a ganhar: {} '.format(salário, novo))


inss = round(salário*11/100, 2)
fgts = round(salário*8/100, 2)
salario_liquido = round(salário -  fgts - inss, 2)


print(" - fgts (8%) : R$", fgts)
print(" - INSS (11%) : R$", inss)
print(" = Salário Liquido : R$", salario_liquido)