#!/usr/bin/env python3

from pprint import pprint
from collections import OrderedDict

file = open('input.txt', 'r')
lines = file.readlines()

ord = []
pos = []
for l in lines:
    l = l.strip()
    v = int(l)*811589153
    ord.append((v,len(ord)))
    pos.append((v,len(pos)))

#print(ord)
#print(pos)
def movep(pos, i, n):
    n = (i+n-1)%(len(pos)-1)+1-i
    #print('move %',n)
    if n>0:
        f = pos[:i]
        e = pos[i:i+1]
        m = pos[i+1:i+1+n]
        l = pos[i+1+n:]
        #print(f,e,m,l)
        #print('e',e,'m',m)
        return f+m+e+l,e[0],m,1
    if n<0:
        f = pos[:i+n]
        m = pos[i+n:i]
        e = pos[i:i+1]
        l = pos[i+1:]
        #print(f,e,m,l)
        return f+e+m+l,e[0],m,-1
    return pos.copy(),(0,0),[],0

def movei(ord, e, m, sign):
    _,i = e
    n,j = ord[i]
    ord[i] = (n,j+len(m)*sign)
    #print('m',m)
    for _,i in m:
        n,j = ord[i]
        ord[i] = (n,j-sign)
    return ord

def keys(pos):
    return [p[0] for p in pos]

def test(ord, pos):
    #print('===> nouveau tour')
    #print('  o',ord)
    #print('  p',keys(pos))
    for n,i in ord:
        #print(n,'move (',i,')')
        pos,e,m,s = movep(pos,i,n)
        movei(ord,e,m,s)
        #print('o',ord)
        #print('p',keys(pos))
    return pos

#print('o',ord)
#print('p',keys(pos))
#print('move')
#pos,e,m,s = movep(pos,1,-3)
#ord = movei(ord,e,m,s)
#print('o',ord)
#print('p',keys(pos))

#print(ord,'\n',keys(pos))
#print(keys(pos))
for _ in range(10):
    pos = test(ord,pos)
#print(keys(pos))
for i,v in enumerate(pos):
    n,_ = v
    if n==0:
        break
total = 0
for n in range(1000,4000,1000):
    val = pos[(i+n)%len(pos)][0]
    print(n,val)
    total += val
print(total)

