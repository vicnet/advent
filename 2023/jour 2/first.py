#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

maxs = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

sum = 0
for l in lines:
    game,sets = l.split(':')
    id = game.split(' ')[-1]
    id = int(id)
    print(id, sets)
    maxok = True
    for set in sets.split(';'):
        print('-',set)
        cubes = set.split(',')
        for cube in cubes:
            nb,color = cube.strip().split(' ')
            print('  -', color, nb)
            if int(nb)>maxs[color]:
                maxok = False
    print('==>', maxok)
    if maxok:
        sum += id
print(sum)
