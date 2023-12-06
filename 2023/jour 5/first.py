#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

maps = {}
map = None
seeds = None
names = []

total = 0
for i,l in enumerate(lines):
    if i==0:
        seeds = l.split(' ')[1:]
        seeds = [ int(seed) for seed in seeds]
        # print(seeds)
        continue
    if len(l)==0:
        map = None
        continue
    if map is None:
        map = l.split('-')[0]
        maps[map] = []
        names.append(map)
        # print(map)
        continue
    # print(l, map)
    vals = l.split(' ')
    vals = [ int(val) for val in vals]
    maps[map].append(vals)
    # print(vals)

# print(maps)

total = None
for seed in seeds:
    print(seed)
    for name in names:
        # print('-', name)
        map = maps[name]
        next = None
        for vals in map:
            # print(' ', vals)
            dst,src,nb = vals
            if seed in range(src,src+nb):
                # print('found', dst, src)
                next = dst + seed-src
                break
        if not next:
            next = seed
        print('-', name, next)
        seed = next
    print('==>', seed)
    if not total:
        total = seed
    else:
        total = min(total, seed)

print(total)
