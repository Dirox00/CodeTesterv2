#!/usr/bin/python3

inp1 = input()
inp2 = input()
inp3 = input()

if (inp1, inp2, inp3) == ('Si', 'Si', 'Si'):
    print('¿Quedamos para comer coles?')
elif (inp1, inp2) == ('Si', 'Si') or inp3 == 'Si':
    print('Te veo en el instituto.')
else:
    print('No me mires.')