#!/usr/bin/env python3

from pprint import pprint


file = open('input.txt', 'r')
lines = file.readlines()

tjets = None
for l in lines:
    l = l.strip()
    tjets = l
jets = None
#print(jets)
lj = len(tjets)

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
        return hash(self.coord())
    def coord(self):
        return (self.x,self.y)

class Rock:
    def __init__(self, l):
        self.ps = [Point(x,y) for x,y in l]
    def copy(self):
        return Rock([p.coord() for p in self.ps])
    def move(self, d):
        ps = [ ]
        for p in self.ps:
            n = p+d
            if n.x<0 or n.x>=7: return False
            if n.y<0: return False
            if n.get()!='.': return False
            ps.append(n)
            #print(n,n.get())
        self.ps = ps
        return True
    def down(self):
        return self.move(Point(0,-1))
    def left(self):
        self.move(Point(-1,0))
    def right(self):
        self.move(Point(1,0))
    def __str__(self):
        return str(self.ps)
    def __repr__(self):
        return repr(self.ps)
    def fixe(self, c='#'):
        ymax = 0
        for p in self.ps:
            p.set(c)
            ymax = max(ymax, p.y)
        return ymax
    def moves(self, i=None):
        global jets
        while True:
            if i is not None:
                i -= 1
                if i==0: return
            if not jets:
                jets = tjets
            j = jets[0]
            jets = jets[1:]
            #print(self,j)
            if j=='>':
                self.right()
            else:
                self.left()
            if not self.down():
                return self.fixe()

forms = [
    Rock( ((0,0), (1,0), (2,0), (3,0),) ),
    Rock( ((0,1), (1,1), (2,1), (1,0), (1,2),) ),
    Rock( ((0,0), (1,0), (2,0), (2,1), (2,2),) ),
    Rock( ((0,0), (0,1), (0,2), (0,3), )),
    Rock( ((0,0), (1,0), (0,1), (1,1), )),
    ]

count = 1000000000000
#count = 2021
count = 40000
limit = 105000

#repeat = 35
repeat = 1725
keep = 5
totaux = []

plan = []
for y in range(limit*3):
    l = ['.']*7
    plan.append(l)

def pplan():
    for l in reversed(plan):
        s = ''
        for t in l:
            s+=t
        print(s)

#pplan()

ymax = 3
total = 0
last = 0
lastj = 0
li = 0
curtot = []
for i in range(count):
    #print(jets)
    r = forms[i%5].copy()
    d = Point(2,ymax)
    r.move(d)
    #print(i, r)
    #if i==28:
        #r.fixe('@')
        #break
    ny = r.moves()+4
    ymax = max(ymax,ny)
    if ymax>limit:
        print(i)
        total += limit
        ymax -= limit
        plan = plan[limit:]
        for _ in range(limit):
            l = ['.']*7
            plan.append(l)
    if keep>0:
        curtot.append(total+ymax-last)
    if i%repeat==0:
        keep -= 1
        if keep>0:
            totaux.append(curtot)
            curtot = []
    #if len(jets)>lastj:
    #if len(jets)==2:
    #if i%(5*400)==0: # and len(jets)==2:
        #print(i-li,len(jets),total+ymax-last)
        li = i
    last = total+ymax
    lastj = len(jets)

#print(r)
#pplan()
#print(total+ymax)
l = 2022
l = 1000000000000
total=0
for t in totaux[:-1]:
    total += sum(t)
    l -= len(t)
    print(len(t),t)
print('first',l,total)
n = int(l/repeat)
r = l%repeat
tr = totaux[-1]
total += sum(tr)*n
total += sum(tr[:r])
print('rep', repeat, n, r, total-3)
