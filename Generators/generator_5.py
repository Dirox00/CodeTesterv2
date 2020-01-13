#!/usr/bin/python3

from random import choice, randint
sequence = ''
for i in range(randint(1, 13)):
    sequence += choice('()')
print(sequence)