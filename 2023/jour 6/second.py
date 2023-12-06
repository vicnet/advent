#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

total = 0
for i,l in enumerate(lines):
    # print(l)
    nbs = re.findall('\d+',l)
    nb = int(''.join(nbs))
    if i==0: t = nb
    if i==1: d = nb
print(t,d)

total = 1
print('t:',t)
val = 0
for h in range(t+1):
    v = (t-h)*h
    # print('- ',h,v)
    if v>d:
        val += 1
print("=> ", val)
total *= val

print(total)
