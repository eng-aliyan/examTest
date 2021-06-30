def areEven(x):
	even = True
	a = x
	while a > 0:
		a, b = int(a/10), a%10
		if b%2 != 0:
			even = False
			break
	return even

for i in range(100, 400+1):
	if areEven(i):
		print(i, end=',')