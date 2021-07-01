import math

inNumbers = []
for i in range(10):
    n = int(input())
    inNumbers.append()

squares = []
for i in inNumbers:
    squares.append(math.pow(i, 2))

sqNumbers = {}
for i in range(10):
    num = inNumbers[i]
    sqNumbers[num] = int(math.pow(num, 3))

print(sqNumbers)
