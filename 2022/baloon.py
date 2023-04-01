#!/usr/bin/env python3

from pprint import pprint
from collections import OrderedDict

file = open('input.txt', 'r')
lines = file.readlines()

conv = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
    }

ns = []
size = 0
for l in lines:
    l = l.strip()
    size = max(size,len(l))
    n = []
    for c in l:
        n.append(conv[c])
    #print(n)
    ns.append(n)
#print(ns)

base = []
val = 1
for _ in range(size):
    base.append(val)
    val *= 5
#print(base)

total = 0
for n in ns:
    #print(n)
    val = 0
    for i,c in enumerate(reversed(n)):
        #print(c)
        val += c*base[i]
    #print(c, n,val)
    total += val
    #break
print(total)

def affiche(n):
    s = ''
    for c in n:
        if 0<=c<3:
            s += str(c)
            continue
        if c==-1:
            s += '-'
            continue
        if c==-2:
            s += '='
            continue
        s += '?'
    return s

def conv(v):
    n = []
    for b in reversed(base):
        c = int(v/b)
        v -= c*b
        n.append(c)
    nn = []
    retenue = 0
    for c in reversed(n):
        c += retenue
        if c<3:
            retenue = 0
            nn.append(c)
            continue
        retenue = 1
        c -= 5
        nn.append(c)
    return list(reversed(nn))

n = conv(total)
print(total, n, affiche(n))
