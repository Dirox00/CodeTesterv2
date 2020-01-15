#!/usr/bin/python3
def fib():
    last, actual = 0, 1
    yield 0
    yield 1
    while True:
        last, actual = actual, last + actual
        yield actual
n = int(input())
for num in fib():
    if n == num:
        print('Yes')
        break
    if num > n:
        print('No')
        break