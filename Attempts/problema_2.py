#!/usr/bin/python3

#problema 2
n = int(input())
m = int(input())

cSum = sum([i for i in range(n+1, n+m+1)])
pSum = sum([i for i in range(n-1, n-m-1, -1)])
    
print(cSum, pSum)