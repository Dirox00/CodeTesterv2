#!/usr/bin/python3
from random import randint
name = ''
for _ in range(randint(1, 100)):
    name += chr(randint(65, 122))
    
print(name)