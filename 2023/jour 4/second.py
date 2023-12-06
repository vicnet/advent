#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

totals = [0]*len(lines)
for l in lines:
    print(l)
    card,nums = l.split(':')
    _,num = re.split("\s+", card)
    num = int(num)
    wins,owns = nums.split('|')
    wins = wins.strip().split(' ')
    owns = owns.strip().split(' ')
    wins = [ int(w) for w in wins if w ]
    owns = [ int(o) for o in owns if o ]
    wins.sort()
    owns.sort()
    val = 0
    for own in owns:
        if own in wins:
            # print('-',own)
            val += 1
    totals[num-1] += 1
    pts = totals[num-1]
    for n in range(num+1,num+val+1):
        totals[n-1] += pts
    print(num,':', wins, owns, val)
    print(totals)

total = sum(totals)
print(total)
