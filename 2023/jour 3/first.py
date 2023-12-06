#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

digits = []
symbs = []
total = 0
for l in lines:
    print(l)
    matches = []
    for val in re.finditer('\d+',l):
        print('=', val)
        matches.append(val)
    digits.append(matches)
    matches = []
    for val in re.finditer('[^\d\.]',l):
        print('=', val)
        matches.append(val)
    symbs.append(matches)

def test(digit, symbs):
    s,l = digit.span()
    for symb in symbs:
        pos = symb.start()
        if pos>=s-1 and pos<=l:
            return True
    return False

def val(digit, symbs):
    if test(digit, symbs):
        return int(digit[0])
    return 0

for y,line in enumerate(digits):
    for digit in line:
        print(digit)
        s,l = digit.span()
        total += val(digit, symbs[y])
        if y>0:
            total += val(digit, symbs[y-1])
        if y<len(digits)-1:
            total += val(digit, symbs[y+1])

print(total)
