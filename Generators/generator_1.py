#!/usr/bin/python3
from random import randint, choice
name = ''
for _ in range(randint(1, 30)):
    name += chr(choice([randint(65, 65 + 25), randint(97, 97 + 25)]))
name += 's'
print(name)