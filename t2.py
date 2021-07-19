passwd = input('[o]: ')
cases = [["$", "#", "@"], range(48, 59), range(65, 92), range(97, 124)]
isValid = True
if not 6 <= len(passwd) <= 16:
	isValid = False
if isValid:
	passed = False
	for item in cases:
		for c in item:
			if ('%c'%c) in passwd:
				passed = True
				break
	if not passed:
		isValid = False
if isValid:
    print("passwd is valid")
else:
    print("passwd is invalid")
