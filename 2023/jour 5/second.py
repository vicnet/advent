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

pairs = []
for i in range(0, len(seeds), 2):
    # Récupérer les éléments deux par deux et les ajouter à la liste
    pair = (seeds[i], seeds[i + 1])
    pairs.append(pair)
# Afficher le résultat
seeds = pairs
# print(seeds)
# print(maps)

def split(seed, vals):
    seed,nbseed = seed
    dst,src,nb = vals
    if seed>=src+nb:
        # after
        return [ None, None, (seed, nbseed) ]
    if seed>=src:
        # inside
        dstseed = dst + seed-src
        # complete inside
        if seed+nbseed<=src+nb:
            return [ None, (dstseed, nbseed), None ]
        # cut in two  [...|...XX|XXX...]
        return [ None, (dstseed, src+nb-seed ),
                 (src+nb, seed+nbseed-src-nb ) ]
    # totaly outside right
    if seed+nbseed<=src:
        return [ (seed, nbseed), None, None ]
    # splited in two, before end src [...XX|XXX...|...]]
    if seed+nbseed<=src+nb:
        return [ (seed,src-seed),
                 (dst, seed+nbseed-src), None ]
    # split in 3
    return [ (seed,seed+nb-src),
             (dst, nb),
             (src+nb, seed+nbseed-src-nb ) ]

# print(split( (97,5), (50,98,2) ))

def convert(seed, map):
    result = []
    seeds = [ seed ]
    for vals in map:
        next = []
        for seed in seeds:
            res = split(seed, vals)
            print('    ', seed, vals, res)
            if res[0] is not None:
                next.append(res[0])
            if res[2] is not None:
                next.append(res[2])
            if res[1] is not None:
                result.append(res[1])
        seeds = next
    result += seeds
    return result

def convert_seed(seed):
    current = [ seed ]
    for name in names:
        print('-', name)
        map = maps[name]
        next = []
        for seed in current:
            res = convert(seed, map)
            print(seed,' -> ',res)
            next += res
        current = next
    return current

total = None
for seed in seeds:
    print(seed)
    res = convert_seed(seed)
    print(seed, '==>', res)
    vals = [ f for f,_ in res ]
    val = min(vals)
    print('vals:', vals, val)
    if not total:
        total = val
    else:
        total = min(total, val)

print(total)

# print(split((74,14), (45,77,23)))