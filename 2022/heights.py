#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

hs = []
xs = None
ys = None
for l in lines:
    l = l.strip()
    row = []
    for c in l:
        h = ord(c)-97
        if c=='S': h=-1
        if c=='E': h=26
        row.append(h)
    hs.append(row)
    xs = len(row)
ys = len(hs)
#print(hs)
paths = {}

class Point:
    def __init__(self, p, h):
        self.p = p
        self.h = h
    def __str__(self):
        return f'{self.p}:{self.h}'
    def __repr__(self):
        return f'P{self.p}:{self.h}'

S = None
Z = None
for y,row in enumerate(hs):
    for x,h in enumerate(row):
        path = []
        if y>0:
            ht = hs[y-1][x]
            if ht-h<=1:
                path.append( Point((x,y-1), ht) )
        if y<len(hs)-1:
            ht = hs[y+1][x]
            if ht-h<=1:
                path.append( Point((x,y+1), ht) )
        if x>0:
            ht = hs[y][x-1]
            if ht-h<=1:
                path.append( Point((x-1,y), ht) )
        if x<len(row)-1:
            ht = hs[y][x+1]
            if ht-h<=1:
                path.append( Point((x+1,y), ht) )
        #print((x,y),h,path)
        paths[(x,y)] = {'ps':path, 'h':h, 'l':None}
        if h==26:
            Z=(x,y)
        if h==-1:
            S=(x,y)
#pprint(paths)

def next(s):
    p,h,l = paths[s].values()
    #print(s,p,h,l)
    for n in p:
        np,_,nl = paths[n.p].values()
        #print('=>',n.p,np,nl)
        if nl is None:
            paths[n.p]['l'] = l+1
            next(n.p)
            continue
        if nl>l+1:
            paths[n.p]['l'] = l+1
            print("=> lower",nl,l+1)
            next(n.p)
            continue
    #same = []
    #path = []
    #for n,hn in ps:
        #if h==hn:
            #same.append(n)
        #else:
            #path.append(n)
    #if len(path)==0:
        #path = same
    #for n in path:
        #next(n)


paths[S]['l'] = 0
#next(s)
#pprint(paths)
#print(paths[cible]['l'])
#next(s)
#print(paths[cible]['l'])

def step():
    for s,p in paths.items():
        if p['l'] is not None:
            l = p['l']+1
            for n in p['ps']:
                nl = paths[n.p]['l']
                #print(s,'=>',n.p, '=> ',nl,l)
                if nl is None:
                    #print(s,'=>',n.p, '=> new',nl,l)
                    paths[n.p]['l'] = l
                    continue
                if nl>l:
                    paths[n.p]['l'] = l
                    #print(s,'=>',n.p, '=> lower',nl,l)
                    continue

def pmat():
    limit = 9
    mat = []
    for y in range(limit):
        mat.append([])
        for x in range(limit):
            mat[y].append(None)
    for s,p in paths.items():
        x,y = s
        if x>=limit or y>=limit: continue
        if p['l']==None:
            mat[y][x] = 'Non '
        else:
            mat[y][x] = f'{p["l"]:3} '
    pprint(mat)

def plet():
    mat = []
    for y in range(ys):
        mat.append([])
        for x in range(xs):
            mat[y].append(None)
    for s,p in paths.items():
        x,y = s
        if p['l']==None:
            mat[y][x] = chr(65+p['h'])
        else:
            mat[y][x] = chr(97+p['h'])
    for r in mat:
        print(''.join(r))

def count():
    c = 0
    for s,p in paths.items():
        if p['l'] is None:
            c += 1
    return c

alist = [S]
def starts(s):
    p = paths[s]
    #print(s,p)
    for n in p['ps']:
        #print(n)
        if n.h==0:
            if n.p not in alist:
                alist.append(n.p)
                starts(n.p)
starts(S)
#print(alist)

min = None
for S in alist:
    #print('New start',S)
    for p in paths.values():
        p['l'] = None
        #print(p)
    paths[S]['l'] = 0
    for i in range(300):
        #print('new step')
        step()
        #plet()
        #pmat()
        #pprint(paths)
        #print(i,count())
    val = paths[Z]['l']
    print(val)
    if min is None or val<min:
        min = val
#plet()
print('Min',min)
