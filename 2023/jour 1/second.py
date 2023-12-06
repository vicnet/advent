#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

digits_values = [ '1','2', '3', '4', '5', '6', '7', '8', '9' ]
digits_names = [ 'one','two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

def conv(l, n):
    if l[n] in digits_values:
        return int(l[n])
    for d in digits_names:
        if l[n:].startswith(d):
            return digits_names.index(d)+1
    return -1

sum = 0
for l in lines:
    first = 100
    last = -1
    for d in digits_values + digits_names:
        pos = l.find(d)
        if pos>=0:
            first = min(first, pos)
        pos = l.rfind(d)
        if pos>=0:
            last = max(last, pos)
    first = conv(l, first)
    last = conv(l, last)
    val = int(first*10 +  last)
    print(l, val)
    sum += val
print(sum)
