#!/usr/bin/python3

# problema 6
inp = input()

count = 0
state = True

for i in inp:
    if i == ')':
        count -= 1
    else:
        count += 1
    if count < 0:
        break
if count == 0:
    print('Completo')
else:
    print('Incompleto')
