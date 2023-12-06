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
        # print('=', val)
        matches.append(val)
    digits.append(matches)
    matches = []
    for val in re.finditer('\*',l):
        print('=', val)
        matches.append(val)
    symbs.append(matches)

mult = {}

def test(y, digit, symbs):
    s,l = digit.span()
    for symb in symbs:
        pos = symb.start()
        if pos>=s-1 and pos<=l:
            hash = (y, pos)
            if hash not in mult:
                mult[hash] = []
            mult[hash].append(int(digit[0]))

for y,line in enumerate(digits):
    for digit in line:
        print(digit)
        s,l = digit.span()
        test(y, digit, symbs[y])
        if y>0:
            test(y-1, digit, symbs[y-1])
        if y<len(digits)-1:
            test(y+1, digit, symbs[y+1])

for vals in mult.values():
    if len(vals)<2:
        continue
    val = 1
    for v in vals:
        val *= v
    total += val

print(total)
