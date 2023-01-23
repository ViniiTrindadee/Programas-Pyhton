'''como utilizar a instrução break e os loopings infinitos a favor das nossas
estratégias de código'''

n = s = 0
while True:
     n = int(input('Digite um número: '))
     if n == 999:
         break
     s += n
# print('A soma vale {}'.format(s))
print(f'A sina vale{s}')