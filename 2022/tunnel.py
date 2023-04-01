#!/usr/bin/env python3

from pprint import pprint

class Point:
    def __init__(self,x,y):
        self.x = int(x)
        self.y = int(y)
    def __sub__(self, p):
        return Point(self.x-p.x, self.y-p.y)
    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)
    def __repr__(self):
        return f'P({self.x},{self.y})'
    def __str__(self):
        return f'({self.x},{self.y})'
    def min(self,p):
        if p is None: return Point(self.x,self.y)
        return Point(min(self.x,p.x),min(self.y,p.y))
    def max(self,p):
        if p is None: return Point(self.x,self.y)
        return Point(max(self.x,p.x),max(self.y,p.y))
    def __eq__(self, p):
        return self.x==p.x and self.y==p.y
    def __ne__(self, x):
        return self.x!=p.x or self.y!=p.y
    def copy(self):
        return Point(self.x, self.y)
    def set(self, c):
        global plan
        plan[self.y][self.x] = c
    def get(self):
        global plan
        return plan[self.y][self.x]
    def distm(self, p=None):
        if p is None: d = self
        else: d = self-p
        return abs(d.x)+abs(d.y)
    def __hash__(self):
        return hash((self.x,self.y))

file = open('input.txt', 'r')
lines = file.readlines()

def test(cible = 2000000):
    covers = []
    spots = set()
    for l in lines:
        l = l.strip()
        parts = l.split()
        #print(parts[2],parts[3],parts[8],parts[9])
        s = Point(parts[2][2:-1],parts[3][2:-1])
        b = Point(parts[8][2:-1],parts[9][2:])
        spots.add(s)
        spots.add(b)
        #
        d = s.distm(b)
        #print(s,b,d)
        if s.y-d <= cible <= s.y+d:
            # distance restante
            r = d-abs(s.y-cible)
            c = range(s.x-r, s.x+r+1)
            #print('contact',c)
            covers.append(c)
        #print(s,b)

    def inter(r1, r2):
        return range(max(r1.start,r2.start), min(r1.stop,r2.stop)) or None
    def union(r1, r2):
        if r1.stop==r2.start:
            return range(min(r1.start,r2.start), max(r1.stop,r2.stop))
        if r2.stop==r1.start:
            return range(min(r1.start,r2.start), max(r1.stop,r2.stop))
        if inter(r1,r2) is None: return None
        return range(min(r1.start,r2.start), max(r1.stop,r2.stop))

    ls = []
    def get_inter():
        for i,r1 in enumerate(covers):
            for j,r2 in enumerate(covers):
                if j<=i: continue
                ru = union(r1,r2)
                if ru is None: continue
                #print('comp',i,r1,j,r2, inter(r1,r2), '=>', ru)
                return i,j,ru
        return None,None,None

    while True:
        #print(covers)
        i,j,r = get_inter()
        if r is None: break
        #print("=>",i,j,r)
        del covers[j]
        covers[i] = r

    total = 0
    for r in covers:
        l = r.stop-r.start
        #print(l)
        for s in spots:
            if s.y==cible:
                if s.x in r:
                    #print('s',s)
                    l -= 1
        #print(r,l)
        total += l
    #print(total)
    print(cible,covers)
    return len(covers)>=2

cible = 2000000
dist = 0
while True:
#for _ in range(40000):
    if test(cible+dist):
        print('trouvé',cible+dist)
        break
    if test(cible-dist):
        print('trouvé',cible-dist)
        break
    dist += 1
y = 3204480
x = 3446137
print(x*4000000+y)
