#!/usr/bin/python3

import math

n = int(input())

primes = []
notPrimes = set()
# para obtener todos los primos menores a n
for i in range(2, n):
    if i in notPrimes:
        continue
    for j in range(i*2, n, i):
        notPrimes.add(j)
    primes.append(i)

sums = []
for i in primes:
    if i > n//2: # para reducir el tiempo de ejecución
        break
    num = n - i
    if num in primes:
        sums.append((i, num))
        
for suma in sums:
    print(suma[0], '+', suma[1])
    