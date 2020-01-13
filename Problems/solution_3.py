#!/usr/bin/python3

n = int(input())

level1 = ' /\ '
level2 = '/__\\'

for i in range(1, n+1):
    print((level1*i).center(4*n))
    print((level2*i).center(4*n))