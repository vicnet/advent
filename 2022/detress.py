#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

def extract(l):
    # vide
    if l[0]==']':
        return None,l
    if l[0].isdigit():
        # nombre
        val = ''
        while l[0].isdigit():
            val += l[0]
            l = l[1:]
        #print(val)
        return int(val),l
    if l[0]!='[':
        print('err')
        return None,l[1:]
    # liste
    l = l[1:]
    vals = []
    while True:
        val,l = extract(l)
        vals.append(val)
        if l[0]==',':
             l = l[1:]
             continue
        if l[0]==']':
             l = l[1:]
             break
    return vals,l

signals = []
left = None
right = None
for l in lines:
    l = l.strip()
    if not l:
        signals.append((left,right))
        left = None
        rigth = None
        continue
    val,last = extract(l)
    if last!='':
        print('yen reste !',l,last)
    #print(l,'=>',val)
    if not left:
        left = val
    else:
        right = val
#print(signals)

def compare(left,right):
    #print('compare',left,'vs',right)
    for l,r in zip(left,right):
        #print('compare',l,'vs',r)
        if l is None and r is None:
            continue
        if l is None:
            return True
        if r is None:
            return False
        if isinstance(l,int) and isinstance(r,int):
            #print('  int,int',l,r)
            if l<r:
                #print('l<r True')
                return True
            if l>r:
                #print('l>r False')
                return False
            #print('l=r')
            continue
        if isinstance(l,int):
            #print('  int,list',l,r)
            res = compare([l],r)
            if res is None:
                continue
            return res
        if isinstance(r,int):
            #print('  list,int',l,r)
            res = compare(l,[r])
            if res is None:
                continue
            return res
        #print('  list,list',l,r)
        res = compare(l,r)
        if res is not None:
            return res
    if len(left)<len(right):
        return True
    if len(left)>len(right):
        return False
    return None

i = 1
total = 0
for left,right in signals:
    #print(left,right)
    res = compare(left,right)
    if res is None:
        print('indecidable ?!?')
    if res==True:
        total += i
    #print(i,'==>',res)
    i += 1
#print(total)

l = [ [[2]], [[6]] ]
for left,right in signals:
    l.append(left)
    l.append(right)
print(l)
def cmps(l,r):
    res = compare(l,r)
    if res==True:
        return -1
    if res==False:
        return 1
    return 0
from functools import cmp_to_key
l = sorted(l,key=cmp_to_key(cmps))
print(l)
f = l.index([[2]])+1
s = l.index([[6]])+1
print(f,s,f*s)

