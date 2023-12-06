#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

total = 0
for l in lines:
    print(l)
    card,nums = l.split(':')
    # _,num = card.split(' ')
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
            if val==0:
                val = 1
                continue
            val *= 2
    # print(num,':', wins, owns, val)
    print(wins, owns, val)
    total += val

print(total)
