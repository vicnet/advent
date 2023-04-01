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

plan = []
pmin = Point(0,0)
pmax = Point(0,0)
pwd = []
first = True
for l in lines:
    l = l[:-1]
    if not l:
        first = False
        continue
    if first:
        if pmax.x!=0:
            l += ' '*(pmax.x-len(l))
        plan.append(list(l))
        pmax.x = len(l)
        continue
    n = ''
    l += ' '
    for c in l:
        if c.isdigit():
            n += c
            continue
        pwd.append(int(n))
        n = ''
        pwd.append(c)
pmax.y = len(plan)

def affich():
    for l in plan:
        print(''.join(l))

dirs = [
    Point(1,0), # Right
    Point(0,1), # down
    Point(-1,0), # left
    Point(0,-1), # up
    ]
sdirs = [ '>', 'v', '<', '^' ]

class Pos:
    def __init__(self, p=None, d=None):
        if p is None:
            # trouve le 1er point
            p = Point(0,0)
            for c in plan[0]:
                if c=='.':
                    break
                p += dirs[0]
            self.p = p
        else:
            self.p = p
        if d is None:
            self.set_dir(0)
        else:
            self.set_dir(d)
        for idf,f in enumerate(faces):
            if f.ins(self.p):
                self.idf = idf
                self.f = f
    def __str__(self):
        return f'{self.p}:{self.sdir()}'
    def sdir(self):
        return sdirs[self.idir]
    def avance(self, i):
        #print('avance',i)
        if isinstance(i,int):
            self.dpl(i)
        else:
            self.rot(i)
    def set(self, c=None):
        if c is None:
            self.p.set(self.sdir())
        else:
            self.p.set(c)
    def dpl(self, i):
        self.set()
        for _ in range(i):
            p = self.p + self.dir
            idir = self.idir
            idf = self.idf
            if not self.f.ins(p):
                p,idir,idf = self.swap(p)
            #while True:
                #p += self.dir
                #p.mod()
                ##print('test',p,p.get())
                #if p.get()!=' ': break
            if p.get()=='#': break
            self.p = p
            self.set_dir(idir)
            self.set_face(idf)
            self.set()
    def swap(self, p):
        idf,d,op = cnxs[self.idf][self.idir]
        f = faces[idf]
        p = p-self.f.p1
        #print('1tr',lp,'in',f)
        p = op(p)
        #print(lp)
        p.x = p.x % l
        p.y = p.y % l
        #print(lp,f)
        p += f.p1
        #print(lp)
        return p,d,idf
    def set_dir(self, idir):
        self.idir = idir % 4
        self.dir = dirs[self.idir]
    def set_face(self, idf):
        self.idf = idf
        self.f = faces[self.idf]
    def rot(self, i):
        if i=='R':
            self.set_dir(self.idir+1)
            return
        if i=='L':
            self.set_dir(self.idir-1)
            return
        return False
    def total(self):
        return (self.p.y+1)*1000 + (self.p.x+1)*4 + self.idir

class Face:
    def __init__(self,p,s):
        self.p1 = Point(p)
        self.p2 = self.p1+Point(s)
    def __str__(self):
        return f'{self.p1}-{self.p2}'
    def ins(self, p):
        #print('test', p, self.p1, self.p2)
        if p<self.p1: return False
        if p>=self.p2: return False
        return True

#l = 4
l = 50
size = (l,l)
faces = [
    Face((l,0),size),
    Face((2*l,0),size),
    Face((l,l),size),
    Face((0,2*l),size),
    Face((l,2*l),size),
    Face((0,3*l),size),
    ]

def test_face():
    f = faces[0]
    print(f)
    for y in range(-2,8):
        s = ''
        for x in range(6,16):
            if f.ins(Point(x,y)):
                s += '.'
            else:
                s += '#'
        print(s)
    print(f.ins(Point(12,0)))

# cnxs[numero de face courante][direction] => face suivante, dir, fct d'inv
def rot1(p):
    return Point(-1,-p.y-1)
def rot2(p):
    return Point(p.y,0)
def rot3(p):
    return Point(-p.x-1,0)
def pas(p):
    return p
def rot4(p):
    return Point(-p.x-1,-1)
def rot5(p):
    return Point(-p.y-1,-1)
def rot6(p):
    return Point(0,-p.x-1)
def rot7(p):
    return Point(-p.y-1,0)
def rot8(p):
    return Point(-p.y-1,-1)
def rot9(p):
    return Point(0,p.x)
def rot0(p):
    return Point(p.y,-1)
def tra3(p):
    return Point(p.x,0)
def tra1(p):
    return Point(-1, p.y)
def tra2(p):
    return Point(0, p.y)
def tra4(p):
    return Point(0, -p.y-1)
def tra5(p):
    return Point(p.x,-1)
def rota(p):
    return Point(-1,p.x)
#cnxs = [
    #[ (5,2,rot1), (3,1,pas),  (2,1,rot2) , (1,1,rot3) ],
    #[ (2,0,pas),  (4,3,rot4), (5,3,rot5) , (0,1,rot3) ],
    #[ (3,0,pas),  (4,0,rot6), (1,2,pas) ,  (0,0,rot9) ],
    #[ (5,1,rot7), (4,1,pas),  (2,2,pas) ,  (0,3,pas) ],
    #[ (5,0,pas),  (1,3,rot4), (2,3,rot5) , (3,3,pas) ],
    #[ (0,2,rot1), (1,0,rot6), (4,2,tra1) ,  (3,2,rot4) ],
    #]
cnxs = [
    [ (1,0,tra2), (2,1,tra3), (3,0,tra4) , (5,0,rot9) ],
    [ (4,2,rot1), (2,2,rota), (0,2,tra1) , (5,3,tra5) ],
    [ (1,3,rot0), (4,1,tra3), (3,1,rot2) , (0,3,tra5) ],
    [ (4,0,tra2), (5,1,tra3), (0,0,tra4) , (2,0,rot9) ],
    [ (1,2,rot1), (5,2,rota), (3,2,tra1) , (2,3,tra5) ],
    [ (4,3,rot0), (1,1,tra3), (0,1,rot2) , (3,3,tra5) ],
    ]

def test_cnxs():
    idf = 2
    f = faces[idf]
    p = Pos(Point(5,5),3)
    p.set()
    print('start',p)
    
    for _ in range(14):
        np = p.p+p.dir
        print('test',np)
        #print(f.ins(p.p)) => False
        if f.ins(np):
            p.p = np
        else:
            nidf,nd,op = cnxs[idf][p.idir]
            nf = faces[nidf]
            lp = np-f.p1
            print('1tr',lp,'in',f)
            lp = op(lp)
            print(lp)
            lp.x = lp.x % 4
            lp.y = lp.y % 4
            print(lp,nf)
            lp += nf.p1
            print(lp)
            np = Pos(lp,nd)
            # recopie
            idf = nidf
            f = nf
            p = np
        p.set()
    affich()

#test_cnxs()

def test():
    p = Pos()
    # avance
    for i in pwd:
        p.avance(i)
        #if isinstance(i,int):
            #affich()
            #input("Press Enter to continue...")
        #print(p)
    print(p.total())
    #affich()
    #print(p)

#affich()
#print(pwd)
#print(p,pmin,pmax)
#print(p)

test()
