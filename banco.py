print('='*30)
print('      BANCO      ')
print('='*30)

valor = int(input('Qual o valor a ser sacado? R$ '))
total = valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        totalced = 0
        if total == 0:
            break
print('='*30)
print('VOLTE SEMPRE!')

