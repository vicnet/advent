#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

class Point:
    def __init__(self,x,y,z=0):
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)
    def __sub__(self, p):
        return Point(self.x-p.x, self.y-p.y, self.z-p.z)
    def __add__(self, p):
        return Point(self.x+p.x, self.y+p.y, self.z+p.z)
    def __repr__(self):
        return f'P({self.x},{self.y},{self.z})'
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
    def min(self,p):
        if p is None: return Point(self.x,self.y,self.z)
        return Point(min(self.x,p.x),min(self.y,p.y),min(self.z,p.z))
    def max(self,p):
        if p is None: return Point(self.x,self.y,self.z)
        return Point(max(self.x,p.x),max(self.y,p.y),max(self.z,p.z))
    def __eq__(self, p):
        return self.x==p.x and self.y==p.y and self.z==p.z
    def __ne__(self, x):
        return self.x!=p.x or self.y!=p.y or self.z!=p.z
    def copy(self):
        return Point(self.x, self.y, self.z)
    def __hash__(self):
        return hash(self.coord())
    def coord(self):
        return (self.x,self.y,self.z)
    def contact(self,p):
        d = abs(self.x-p.x)+abs(self.y-p.y)+abs(self.z-p.z)
        if d==0:
            print('idem')
            return None
        if d==1: return True
        return False
    def __ge__(self, p):
        return self.x>=p.x or self.y>=p.y or self.z>=p.z
    def __le__(self, p):
        return self.x<=p.x or self.y<=p.y or self.z<=p.z
    def __gt__(self, p):
        return self.x>p.x or self.y>p.y or self.z>p.z
    def __lt__(self, p):
        return self.x<p.x or self.y<p.y or self.z<p.z


ps = []
pmax = None
pmin = None
for l in lines:
    l = l.strip()
    x,y,z = l.split(',')
    p = Point(x,y,z)
    ps.append(p)
    pmax = p.max(pmax)
    pmin = p.min(pmin)

def surface(pts):
    obs = []
    surf = 0
    for p in pts:
        #print('test',p)
        surf += 6
        for o in obs:
            if p.contact(o):
                surf -= 2
                #print(p,o,'contact',surf)
            #else:
                #print(p,o,'pascont',surf)
        obs.append(p)
    return surf

#surf_ps = surface(ps)
#print('surface totale', surf_ps)

def get_air(pts):
    air = []
    for x in range(pmax.x+1):
        for y in range(pmax.y+1):
            for z in range(pmax.z+1):
                p = Point(x,y,z)
                count = 0
                for o in pts:
                    if p==o: break
                    if p.contact(o):
                        count += 1
                    if count==6:
                        #print('trouvé',p)
                        air.append(p)
                        break
    return air

#air = get_air(ps)
#surf_air = surface(air)
#print('surface air', surf_air)

#air2 = get_air(air)

#surf_air2 = surface(air2)
#print('surface air2', surf_air2)

#print('total', surf_ps-surf_air+surf_air2)

#print(pmax+Point(1,1,1), pmin-Point(1,1,1))

#ps=[Point(1,1,1)]
def contact(p):
    count = 0
    for o in ps:
        if p.contact(o):
            count += 1
        if count==6:
            #print('trouvé',p)
            break
    return count


def contacts():
    air = {}
    for x in range(pmax.x+1):
        for y in range(pmax.y+1):
            for z in range(pmax.z+1):
                p = Point(x,y,z)
                if p in ps: continue
                count = contact(p)
                if count==0: continue
                air[p] = count
#print(len(air))
#print(ps)
#print(air)

pmin -= Point(1,1,1)
pmax += Point(1,1,1)
#print(pmin,pmax)

def propage(p):
    tests = [ Point(1,0,0), Point(-1,0,0), Point(0,1,0), Point(0,-1,0), Point(0,0,1), Point(0,0,-1) ]
    grp = [ p ]
    while True:
        #print(grp)
        found = False
        for p in grp:
            #print('propage',p)
            for d in tests:
                ts = p + d
                #print('   test',ts)
                if ts>pmax or ts<pmin:
                    #print('   => sortie')
                    continue
                if ts in ps:
                    #print('   => contact')
                    continue
                if ts in grp:
                    #print('   =>  deja vu')
                    continue
                found = True
                grp.append(ts)
        #print(grp)
        if not found: break
    return grp

pext = Point(1,1,1)
ext = propage(pext)
#print(len(ext),len(ps))

s = sum([contact(p) for p in ext])
print(s)
