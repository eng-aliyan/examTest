passwd = input()

uppers = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

cases = ["$", "#", "@"]

inRange = True
if len(passwd) < 6 or len(passwd) > 16:
    inRange = False

isUpper = False
for item in uppers:
    if item in passwd:
        isUpper = True
        
isLower = False
for item in lower:
    if item in passwd:
        isLower = True
        
isNum = False
for item in nums:
    if item in passwd:
        isNum = True
        
isCases = False
for item in cases:
    if item in passwd:
        isCases = True

isValid = inRange and isUpper and isLower and isNum and isCases

if isValid:
    print("passwd is valid")
else:
    print("passwd is invalid")

