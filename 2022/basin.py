#!/usr/bin/env python3

from pprint import pprint
from collections import OrderedDict

file = open('input.txt', 'r')
lines = file.readlines()

class Point:
    def __init__(self,x,y=None):
        if isinstance(x,tuple):
            self.x = int(x[0])
            self.y = int(x[1])
        else:
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
    def __hash__(self):
        return hash((self.x,self.y))
    def mod(self):
        self.x = self.x % pmax.x
        self.y = self.y % pmax.y
    def __ge__(self, p):
        return self.x>=p.x or self.y>=p.y
    def __le__(self, p):
        return self.x<=p.x or self.y<=p.y
    def __gt__(self, p):
        return self.x>p.x or self.y>p.y
    def __lt__(self, p):
        return self.x<p.x or self.y<p.y

dirs = {
    '>': Point(1,0),
    'v': Point(0,1),
    '<': Point(-1,0),
    '^': Point(0,-1),
    }

class Bliz():
    def __init__(self, x,y, d):
        self.p = Point(x,y)
        self.d = d
        self.dir = dirs[d]
    def avance(self):
        self.p += self.dir
        if self.p.x>=pmax.x-1: self.p.x=1
        if self.p.x<1: self.p.x=pmax.x-2
        if self.p.y>=pmax.y-1: self.p.y=1
        if self.p.y<1: self.p.y=pmax.y-2

bs = []
pmax = Point(0,len(lines))
for y,l in enumerate(lines):
    l = l.strip()
    pmax = Point(len(l),len(lines))
    for x,c in enumerate(l):
        if c=='#': continue
        if c=='.': continue
        bs.append(Bliz(x,y,c))
#print(pmax)

def applati():
    plan = []
    for y in range(pmax.y):
        row = []
        for x in range(pmax.x):
            c = '.'
            if x==0 or y==0: c = '#'
            if x==pmax.x-1 or y==pmax.y-1: c = '#'
            row.append(c)
        plan.append(row)
    plan[0][1] = '.'
    plan[-1][-2] = '.'
    for b in bs:
        plan[b.p.y][b.p.x] = b.d
    return plan

def affiche():
    global plan
    for l in plan:
        print(''.join(l))
    print()

def avance():
    global plan
    for b in bs:
        b.avance()
    plan = applati()

def possible(p):
    ps = []
    for d in dirs.values():
        np = p+d
        if np.x<0 or np.y<0: continue
        if np.x>pmax.x-1 or np.y>pmax.y-1: continue
        #print('test',np,np.get())
        if np.get()=='.':
            ps.append(np)
    if p.get()=='.':
        ps.append(p)
    return ps
    
def plan_seul():
    global plan
    plan = applati()
    affiche()
    for _ in range(5):
        avance()
        affiche()

#plan_seul()

def test():
    global plan

    start = Point(1,0)
    end = Point(pmax.x-2, pmax.y-1)
    total = 0
    
    objs = [ end, start, end ]

    trajs = set()
    trajs.add(start)
    for obj in objs:
        #for i in range(20):
        trouve = False
        i=0
        plan = applati()
        while True:
            i += 1
            print('Minute',i)
            avance()
            #affiche()
            
            ntrajs = set()
            for p in trajs:
                #print('  test',p)
                #p = traj[-1]
                #p.set('E')
                #affiche()
                ps = possible(p)
                if obj in ps:
                    print('====> trouve',i)
                    total += i
                    trouve = True
                    break
                #print('  pos',ps)
                for np in ps:
                    ntrajs.add(np)
                #print(ntrajs)
                #break
            if trouve: break
            trajs = ntrajs
            print('  trajs',len(trajs))
            #for p,t in trajs.items():
                #print('-',p)
            #if i>2: break
        #print(end)
        trajs = set()
        trajs.add(obj)
    print(total)

test()
