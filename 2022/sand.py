#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __sub__(self, p):
        return Point(self.x-p.x, self.y-p.y)
    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y)
    def __repr__(self):
        return f'P({self.x},{self.y})'
    def __str__(self):
        return f'({self.x},{self.y})'
    def min(self,p):
        return Point(min(self.x,p.x),min(self.y,p.y))
    def max(self,p):
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

rock = []
cmin = Point(500,0)
cmax = cmin
for l in lines:
    l = l.strip()
    parts = l.split()
    path = []
    for i,coord in enumerate(parts):
        if i%2!=0: continue
        x,y = coord.split(',')
        p = Point(int(x),int(y))
        cmin = cmin.min(p)
        cmax = cmax.max(p)
        path.append(p)
    rock.append(path)
    #print(path)
#print(rock)
print(cmin,cmax)
aug = 300
cmin += Point(-aug,0)
cmax += Point(aug,2)
plan = []
for y in range(cmax.y-cmin.y+1):
    l = []
    for x in range(cmax.x-cmin.x+1):
        l.append('.')
    plan.append(l)
#pprint(plan)
for x in range(cmax.x-cmin.x+1):
    plan[-1][x] = '#'

def affich():
    for r in plan:
        s = ''
        for t in r:
            s += t
        print(s)
#affich()
def sign(n):
  if n<0: return -1
  elif n>0: return 1
  else: return 0

for path in rock:
    #print(path)
    for i in range(len(path)-1):
        start = path[i]
        start = start-cmin
        end = path[i+1]
        end = end-cmin
        delta = Point(sign(end.x-start.x),sign(end.y-start.y))
        #print('  ',start,end,delta)
        while True:
            #print('--',start)
            start.set('#')
            if start==end:
                break
            start = start+delta

orig = Point(500,0)
orig -= cmin
orig.set('+')
#affich()

try:
    while True:
        s = orig.copy()
        while True:
            found = False
            for d in [ Point(0,1), Point(-1,1), Point(1,1) ]:
                p = s+d
                #print(s,d,p,p.get())
                if p.get()=='.':
                    found = True
                    s = p
                    break
            if not found: break
        s.set('o')
        if s==orig: break
except Exception as e:
    #print(e)
    pass
#affich()

count = 0
for r in plan:
    for t in r:
        if t=='o': count += 1
print(count)
