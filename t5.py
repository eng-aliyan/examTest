#!/usr/bin/python3

inNumbers = []
for i in range(10):
    n = input('[i-int-%d]: ' %(i+1))
    inNumbers.append(int(n))

squares = []
for i in inNumbers:
    squares.append(i**2)

sqNumbers = {}
for i in range(10):
    sqNumbers[inNumbers[i]] = squares[i]

print(sqNumbers)