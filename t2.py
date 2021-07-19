
passwd = input('[o]: ')

a, b, c = 48, 65, 97
cases = [["$", "#", "@"], range(a, a+11), range(b, b+27), range(c, c+27)]

isValid = True
if not 6 <= len(passwd) <= 16:
	isValid = False

if isValid:
	passed = False
	for item in cases:
		for c in item:
			if '%c'%c in passwd:
				passed = True
				break
	if not passed:
		isValid = False
  
if isValid:
    print("passwd is valid")
else:
    print("passwd is invalid")

