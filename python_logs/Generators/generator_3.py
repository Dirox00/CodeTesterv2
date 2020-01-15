#!/usr/bin/python3
from random import randint, choice
def create_name():
    name = ''
    for _ in range(randint(1, 30)):
        name += chr(choice([randint(65, 65 + 25), randint(97, 97 + 25)])) 
    return name
print(create_name())
print(choice([create_name(), 'Python3']))
