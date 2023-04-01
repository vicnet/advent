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

autours = [
    Point(-1,-1),Point(0,-1),Point(1,-1),
    Point(-1,0),Point(1,0),
    Point(-1,1),Point(0,1),Point(1,1),
    ]
tests = [
    (Point(0,-1), [ Point(-1,-1),Point(0,-1),Point(1,-1) ]),
    (Point(0,1),  [ Point(-1,1), Point(0, 1),Point(1, 1) ]),
    (Point(-1,0), [ Point(-1,-1),Point(-1,0),Point(-1,1) ]),
    (Point(1,0),  [ Point(1,-1),Point(1,0),Point(1,1) ]),
    ]

class Elve():
    def __init__(self, x,y):
        self.p = Point(x,y)
        self.dir = None
    def choix(self):
        #print('choix de ',self.p-pmin)
        self.dir = None
        for d,test in tests:
            #print(' test dpl',d)
            trouve = False
            for t in test:
                #print('   check',p,p.get())
                if self.get(t)=='#':
                    trouve = True
                    break
            #print(' trouve',trouve)
            if not trouve:
                #print('->',self.p-pmin+d)
                c = self.get(d)
                if c=='?':
                    self.set('X',d)
                else:
                    self.set('?',d)
                self.dir = d
                break
    def get(self, d):
        p = self.p-pmin+d
        return p.get()
    def set(self, c, d):
        p = self.p-pmin+d
        return p.set(c)
    def avance(self):
        if self.dir is None: return
        #print(self.p,':',self.get(self.dir),'->',self.dir)
        if self.get(self.dir)!='X':
            #print(self.p,'->',self.dir)
            self.p += self.dir
        self.dir = None
    def bouge(self):
        for d in autours:
            p = self.p-pmin + d
            #print('  =>',p,p.get())
            if p.get()=='#': return True
        return False

es = []
for y,l in enumerate(lines):
    l = l.strip()
    for x,c in enumerate(l):
        if c=='#':
            es.append(Elve(x,y))

def applati():
    pmin = None
    pmax = None
    for e in es:
        if pmin is None:
            pmin = pmax = e.p
            continue
        pmin = e.p.min(pmin)
        pmax = e.p.max(pmax)
    pmin += Point(-1,-1)
    pmax += Point(1,1)
    dim = pmax-pmin+Point(1,1)
    #print(pmin,pmax,dim)
    plan = []
    for _ in range(dim.y):
        row = []
        for _ in range(dim.x):
            row.append('.')
        plan.append(row)
    #print(plan)
    for e in es:
        p = e.p-pmin
        #print('set',p)
        plan[p.y][p.x] = '#'
        #p.set('#')
    return plan, pmin, pmax

def affiche():
    for l in plan:
        print(''.join(l))
    print()

def count():
    total = 0
    for y,l in enumerate(plan):
        if y==0 or y==len(plan)-1: continue
        for x,c in enumerate(l):
            if x==0 or x==len(l)-1: continue
            if c=='.': total += 1
    print(total)

#for i in range(20):
i = 0
while True:
    i += 1
    plan, pmin, pmax = applati()
    #print('round',i)
    #affiche()
    bouge = False
    for e in es:
        if not e.bouge(): continue
        e.choix()
        bouge = True
    if not bouge:
        print('Fin pesonne ne bouge',i)
        break
    #affiche()
    #print('')
    for e in es:
        e.avance()
    plan, pmin, pmax = applati()
    #affiche()
    tests = tests[1:]+tests[0:1]
    #for d,t in tests: print(d)

#affiche()
#count()
