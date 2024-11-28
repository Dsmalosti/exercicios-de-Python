lanche = ('Hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[:2])
print(lanche[-2])
for comida in lanche:
    print(f'Eu vou come {comida}')

for cont in range (0, len(lanche)):
    print(f'Eu vou come {lanche[cont]}')

print(sorted(lanche))

a = (5, 4, 6)
b = (7, 5, 7, 4)
c = a + b
d = b + a
print(f'{c}{d}')
print(c.count(4))
print(c.index(7))