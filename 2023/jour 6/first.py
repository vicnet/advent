#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

total = 0
for i,l in enumerate(lines):
    print(l)
    nbs = re.findall('\d+',l)
    nbs = [ int(n) for n in nbs ]
    if i==0: ts = nbs
    if i==1: ds = nbs
# print(ts,ds)

total = 1
for t,d in zip(ts,ds):
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
