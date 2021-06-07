#!/usr/bin/python3

def areEven(x):
    even = True
    for i in str(x):
        if int(i)%2 != 0:
            even = False
            break
    return even

for i in range(100, 400+1):
    if areEven(i):
        print(i, end=',')