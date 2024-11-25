n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
r = n1 % n2
print('A soma dos numeros é:{}\nA subtração é:{}\nA multiplicação é:{}\nA divisão é{}\n'.format(s, su, m, d), end='')
print('A divisão inteira é:{}\nA potencia é:{}\nO resto é:{}'.format(di, p, r))