#!/usr/bin/env python3

from pprint import pprint


file = open('input.txt', 'r')
lines = file.readlines()

class Valve:
    def __init__(self,name,rate,tunnels):
        self.name = name
        self.rate = rate
        self.tunnels = tunnels
        self.dist = {}
    def __str__(self):
        return f'{self.name}({self.rate})=>{self.tunnels}'
    def __repr__(self):
        return f'V:{self.name}({self.rate})=>{self.tunnels}'
    def d(self, v):
        return self.dist[v.name]

valves = {}
for l in lines:
    l = l.strip()
    parts = l.split()
    name = parts[1]
    rate = int(parts[4][5:-1])
    tunnels = [v[:2] for v in parts[9:]]
    valve = Valve(name,rate,tunnels)
    #print(valve)
    valves[name] = valve
#pprint(valves)

closed = []
for v in valves.values():
    if v.rate!=0:
        closed.append(v)
        #print(v)

def get_dist(frm):
    dist = {}
    for v in valves.values():
        dist[v.name] = None
    dist[frm] = 0
    while True:
        none = 0
        for n,d in dist.items():
            if d is None:
                none += 1
                continue
            #print(n,d)
            for nxt in valves[n].tunnels:
                #print(nxt,d+1)
                if dist[nxt] is None or dist[nxt] > d+1:
                    #if dist[nxt] is not None: print('trouve')
                    dist[nxt] = d+1
        #print(dist)
        if none==0: break
    #print(frm, dist)
    return dist

start = valves['AA']
start.dist = get_dist(start.name)
for v in closed:
    v.dist = get_dist(v.name)


#maxtime = 30
maxtime = 26
max = 0
def parcours(frm, lst, time=0, pres=0, dpres = 0):
    global max
    if not lst:
        npres = pres + dpres*(26-time)
        #print('fin',time, pres, dpres, '=> val',npres)
        if npres>max:
            max = npres
    for nxt in lst:
        reste = lst.copy()
        reste.remove(nxt)

        dt = frm.d(nxt)+1 # dpl + ouverture
        ntime = time + dt 
        if ntime>=26:
            #print('dépassement',ntime+1, frm.name,nxt.name,frm.d(nxt))
            parcours(None, [], time, pres, dpres)
        else:
            npres = pres+dpres*dt
            ndpres = dpres+nxt.rate
            #print(ntime+1, frm.name,nxt.name,frm.d(nxt), npres, ndpres)
            parcours(nxt, reste, ntime, npres, ndpres)
        #break

def one():
    #closed = [ valves['DD'], valves['BB'], valves['JJ'], valves['HH'], valves['EE'], valves['CC'] ]
    parcours(start, closed)
    print(max)

total = 0
def two():
    def test(you,ele):
        global max
        max = 0
        parcours(start, you)
        #print(max)
        max1 = max
        max = 0
        parcours(start, ele)
        #print(max)
        max2 = max
        #print("max",max1+max2)
        return max1+max2

    #you = [ valves['DD'], valves['HH'], valves['EE'], ]
    #ele = [ valves['JJ'], valves['BB'], valves['CC'], ]
    #print(test(you,ele))
    
    def separ(first,last):
        if len(first)+1>=len(last):
            return
        #print(len(first),len(last))
        global total
        for e in last:
            nfirst = first.copy()
            nfirst.append(e)
            nlast = last.copy()
            nlast.remove(e)
            val = test(nfirst,nlast)
            #print('test', val, "  =  ", nfirst, '   =>   ', nlast)
            if val>total:
                total = val
                print(total)
            separ(nfirst,nlast)

    separ([],closed)

two()
print(total)
