import math


a = int(input('[i-int-a]: '))
b = int(input('[i-int-b]: '))

lcm = abs(a*b) // math.gcd(a, b)
print(lcm)
