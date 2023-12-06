#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__, 2)

total = 0
for l in lines:
    print(l)
    game,sets = l.split(':')
    id = game.split(' ')[-1]
    id = int(id)
    # print(id, sets)
    maxs = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for set in sets.split(';'):
        # print('-',set)
        cubes = set.split(',')
        for cube in cubes:
            nb,color = cube.strip().split(' ')
            # print('  -', color, nb)
            nb = int(nb)
            if nb>maxs[color]:
                maxs[color] = nb
    val = 1
    for m in maxs.values():
        val *= m
    print('==>', maxs, val)
    total += val
print(total)
