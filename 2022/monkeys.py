#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

hs = []
for l in lines:
    l = l.strip()
    row = []
    for c in l:
        h = ord(c)-97
        if c=='S': h=-1
        if c=='E': h=26
        row.append(h)
    hs.append(row)
#print(hs)
paths = {}
for y,row in enumerate(hs):
    for x,h in enumerate(row):
        path = []
        if y>0:
            ht = hs[y-1][x]
            if ht-h in [0,1]:
                path.append(((y-1,x),ht))
        if y<len(hs)-1:
            ht = hs[y+1][x]
            if ht-h in [0,1]:
                path.append(((y+1,x),ht))
        if x>0:
            ht = hs[y][x-1]
            if ht-h in [0,1]:
                path.append(((y,x-1),ht))
        if x<len(row)-1:
            ht = hs[y][x+1]
            if ht-h in [0,1]:
                path.append(((y,x+1),ht))
        #print((x,y),h,path)
        paths[(x,y)] = (path,h)
#pprint(paths)

def next(s):
    ps,h = paths[s]
    print(s,ps,h)
    if h==25:
        print('found')
        return
    same = []
    path = []
    for n,hn in ps:
        if h==hn:
            same.append(n)
        else:
            path.append(n)
    if len(path)==0:
        path = same
    for n in path:
        next(n)

s = (0,0)
next(s)
