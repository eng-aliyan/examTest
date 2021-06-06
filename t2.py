#!/usr/bin/python3

password = input('[i]: ')

cases = [['$', '#', '@'], list(range(48, 58)), list(range(65, 91)), list(range(97, 123))]


isValid = True
if len(password) < 6 or len(password) > 16:
    isValid = False

for items in cases:
    passed = False
    for c in items:
        if ('%c' %c) in password:
            passed = True
            break
    if not passed:
        isValid = False
        break

if isValid:
    print('password is valid')
else:
    print('password is invalid!!!')


'''
if isValid:
    isUpper = False
    for i in range(65, 91):
        if ('%c' %i) in password:
            isUpper = True
            break
    if not isUpper:
        isValid = False

if isValid:
    isLower = False
    for i in range(97, 123):
        if ('%c' %i) in password:
            isLower = True
            break
    if not isLower:
        isValid = False

if isValid:
    isNumeric = False
    for i in range(48, 58):
        if ('%c' %i) in password:
            isNumeric = True
            break
    if not isNumeric:
        isValid = False

if isValid:
    isChar = False
    chars = ['$', '#', '@']
    for i in chars:
        if i in password:
            isChar = True
            break
    if not isChar:
        isValid = False

if isValid:
    print('password is valid')
else:
    print('password is not valid!!!')
'''