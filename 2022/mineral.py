#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

class Robot:
    def __init__(self, name, ore, clay, obs, prod):
        self.name = name
        self.cost = (int(ore), int(clay), int(obs))
        self.prod = prod
    def __str__(self):
        return self.name
        #return f'{self.cost}=>{self.prod}'
    def __repr__(self):
        return f'{self.name}:{self.cost}=>{self.prod}'
    def could(self, res):
        for i,c in enumerate(self.cost):
            #print('test',i,c,res[i])
            if res[i]<c: return False
            #if c!=0 and res[i]>2*c: return False
            #if res[i]>15: return False
        return True
    def gener(self, res):
        #val = []
        #for i,p in enumerate(self.prod):
            #val.append(res[i]+p)
        #return val
        for i,p in enumerate(self.prod):
            res[i] += p
    def depens(self, res):
        val = []
        for i,c in enumerate(self.cost):
            val.append(res[i]-c)
        val.append(res[-1])
        return val
    def __lt__(self, r):
        return self.prod<r.prod

class Blueprint:
    def __init__(self, p):
        self.rs = [
            Robot('Or',p[6],0,0, (1,0,0,0)),
            Robot('Cl',p[12],0,0, (0,1,0,0)),
            Robot('Ob',p[18],p[21],0, (0,0,1,0)),
            Robot('Ge',p[27],0,p[30], (0,0,0,1))
            ]
        #self.rs.sort()
        #print(self.rs)
    def __str__(self):
        return f'{self.rs}'
    def __repr__(self):
        return f'{self.rs}'
    def which(self, res):
        w = []
        for r in self.rs:
            if r.could(res):
                w.append(r)
        w.append(None)
        return w


bs = []
for l in lines:
    l = l.strip()
    p = l.split()
    #for i,p in enumerate(parts):
        #print(i,p)
    b = Blueprint(p)
    bs.append(b)
    #print(b)
maxi = 0

def gener(b, t, rs, res):
    global maxi
    if t>24:
        return res[-1]
    #rs.sort()
    names = ','.join([str(r) for r in rs])
    print('init', t, names, res)
    # prod
    res = res.copy()
    for r in rs:
        res = r.gener(res)
        #print('  =>gene', r, nres)
    geode = res[-1]
    # construction eventuelle
    wrs = b.which(res)
    print('  test',wrs)
    for wr in wrs:
        nrs = rs.copy()
        nres = res.copy()
        print('  test',wr,wrs)
        if wr is None:
            # pas de contr
            pass
        else:
            # constr robot
            nres = wr.depens(nres)
            nrs.append(wr)
            print('  =>add', wr, nres)
        # temps suivant
        ngeo = gener(b,t+1,nrs,nres)
        if ngeo>geode:
            #if t==1: print('trouvé',ngeo)
            geode = ngeo
        if geode>maxi:
            maxi=geode
            print('trouvé',maxi)
    return geode


#b = bs[0]
#print(b)
#rs = [ Robot('Or',0,0,0, (1,0,0,0)) ]
#r = rs[0]
#res = r.gener(res)
#print(res)
#new_rs = b.which(res)
#print(rs)
#geode = gener(b,1,rs,res)
#print(geode)


def test_strat(b,rs):
    res = [0,0,0,0]
    deb = [1,0,0,0]
    cur = 0
    rcur = rs[cur]
    r = b.rs[rcur]
    for t in range(24):
        print('== Minute ==',t+1,cur,r)
        # creation
        new = False
        if r is not None and r.could(res):
            print('- constr',r,res)
            res = r.depens(res)
            new = True
        # produit
        for i,p in enumerate(deb):
            res[i] += p
        # ajout
        if new:
            deb[rcur] += 1
            cur += 1
            if cur<len(rs):
                rcur = rs[cur]
                r = b.rs[rcur]
            else:
                r = None
            #else:
                #rcur = 3
                #r = b.rs[rcur]
        print("   => ",res, deb)
    print("   => ",res,cur)
    return res[-1],cur

def add(rss,ir):
    #res = rss.copy()
    res = set()
    for rs in rss:
        trs = list(rs)
        #trouve = ir<2
        for i in range(len(rs)+1):
            #if ir==2 and trs[i]==1:
                #trouve = True
                #continue
            #if not trouve: continue
            nrs = trs[:i] + [ ir ] + trs[i:]
            res.add(tuple(nrs))
    return res

def test_blue(b):
    rs = (1,2,3,3)
    rss = set([rs])
    for _ in range(3):
        rss = add(rss,0)
    for _ in range(4):
        rss = add(rss,1)
    for _ in range(3):
        rss = add(rss,2)
    rss = add(rss,1)
    print(len(rss))
    #print(rss)
    gmax = 0
    for rs in rss:
        if rs[0]==2: continue
        if rs[0:3]==(1,2,3):
            #print('rejet')
            continue
        print('test',rs)
        val = test_strat(b, rs)
        if val>gmax:
            gmax = val
            #print(rs, val)
    return gmax

#b = bs[1]
#val = test_blue(b)
#print(b,val)

# 1,2,3.x => KO, prolongement inutile
# ...x : inutile de tester si x<3, doit être prolongé
# ...x : si x non réalisé => KO prolongement inutile (contient (1,2,3))
# ...  : si réalisé, prolongement OK
# ...x...2.... : il existe x=1
# ...x...y...3... : il existe un x=1 et y=2

def prolong(rs):
    res = set()
    for r in range(4):
        t = list(rs)
        t.append(r)
        res.add(tuple(t))
    return res
def prolong_all(rss):
    res = set()
    for rs in rss:
        nrss = prolong(rs)
        res.update(nrss)
        #print(rs,nrss,res)
    return res

def test_prolong_set():
    rss = set()
    rss.add((0,))
    rss.add((1,))
    rss = prolong_all(rss)

    b = bs[1]
    gmax = 0
    imax = 15
    for i in range(imax):
        print(i,len(rss))
        #print(rss)
        #print(list(rss)[0:2])
        nrss = set()
        for rs in rss:
            geo, nr = test_strat(b,rs)
            if geo>gmax:
                gmax = geo
                print('trouve',gmax,rs)
            if nr>=len(rs) and i<imax-1:
                nrs = prolong(rs)
                nrss.update(nrs)
                #print(rs,geo,'ok',nrs)
        rss = nrss

temps = 32

class Etat:
    def __init__(self, t, res, rs):
        self.t = t # t actuel
        self.res = res # nbr de ressources
        self.rs = rs # nbre de robots
    def __str__(self):
        return f'{self.t}:{self.res}/{self.rs}'
    def __repr__(self):
        return f'{self.t}:{self.res}/{self.rs}'
    def gener(self, b, ir):
        r = b.rs[ir]
        #print('gener',ir,r,'avec',self)
        for t in range(self.t, temps):
            #print('== Minute ==',t+1)
            # creation
            new = False
            if r.could(self.res):
                #print('- constr')
                self.res = r.depens(self.res)
                new = True
            # produit
            for i,p in enumerate(self.rs):
                self.res[i] += p
            # ajout
            if new:
                self.t = t+1
                self.rs[ir] += 1
                #print(' ok =>', self, self.geode())
                return True
            #print(' =>',self)
        #print('  => KO')
        return False

    def geode(self):
        return self.res[-1]+(temps-self.t)*self.rs[3]

    def gmax(self):
        g = self.geode()
        for t in range(self.t+1,temps):
            g += temps-t
        return g

    def copy(self):
        return Etat(self.t, self.res.copy(), self.rs.copy())

#b[1] 9 (0, 1, 1, 1, 2, 1, 2, 2, 2, 3, 3)
#b[1] 12 (0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 2, 3, 3)

def test_one(b, rs):
    e = Etat(0,[0,0,0,0],[1,0,0,0])
    for r in rs:
        if not e.gener(b,r):
            break
    print(b,e.geode())

#exemple = (1,1,1,2,1,2,3,3)
#rs = (0,1,1,1,2,1,2,2,2,3,3)
#test_strat(bs[0], rs)
#test_one(bs[1], rs)

def recur(b, e):
    for ir in range(3):
        ne = e.copy()
        test = ne.gener(b,ir)
        print('test',ne, test)
        if not test: continue
        recur(b,ne)

def test_iter(b):
    e = Etat(0,[0,0,0,0],[1,0,0,0])
    #recur(bs[0],e)
    etats = [e]
    gmax = 0
    l = 0
    while True:
        l += 1
        print(l,'lg',len(etats)) #,etats)
        netats = []
        for e in etats:
            for ir in range(4):
                ne = e.copy()
                test = ne.gener(b,ir)
                #print('test',ne, test)
                if not test: continue
                if ne.gmax()<gmax:
                    #print('rejet')
                    continue
                g = ne.geode()
                #print('val',g,ne)
                if g>gmax:
                    gmax = g
                    #print('trouvé',g,ne)
                netats.append(ne)
        etats = netats
        if len(etats)==0:
            break
    return gmax

#e = Etat(20,[12, 20, 5, 0],[3, 5, 5, 0])
#print(e.geode())
#print(e.gmax())
#print(b)
total = 1
for i,b in enumerate(bs):
    g = test_iter(b)
    print(i,g)
    total *= g
print('total:',total)
