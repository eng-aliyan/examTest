import math


a = int(input())
b = int(input())

lcm = abs(a*b) // math.gcd(a, b)
print(lcm)
