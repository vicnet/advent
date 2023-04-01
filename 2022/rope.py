#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

# ...
# ...
# T..

# delta pos de H par rapport au referentiel T
# => dpl de T
table = {
    (0,0): (0,0),
    (0,1): (0,0),
    (0,2): (0,1),
    (1,0): (0,0),
    (1,1): (0,0),
    (1,2): (1,1),
    (2,0): (1,0),
    (2,1): (1,1),
    (2,2): (1,1), # cas impossible
    }

for x in range(3):
    for y in range(3):
        tx,ty = table[(x,y)]
        table[(-x,y)] = (-tx,ty)
        table[(x,-y)] = (tx,-ty)
        table[(-x,-y)] = (-tx,-ty)
        #print(-x,y,table[(-x,y)])

rope = [ (0,0) ]*10
pos = []
#print(table[tuple(h)])
for l in lines:
    l = l.strip()
    d,n = l.split()
    for _ in range(int(n)):
        # move h
        h = rope[0]
        if d=='U':
            h = (h[0],h[1]+1)
        elif d=='D':
            h = (h[0],h[1]-1)
        elif d=='R':
            h = (h[0]+1,h[1])
        elif d=='L':
            h = (h[0]-1,h[1])
        rope[0] = h
        for i in range(len(rope)-1):
            h = rope[i]
            t = rope[i+1]
            delta = (h[0]-t[0],h[1]-t[1])
            move = table[delta]
            t = (t[0]+move[0],t[1]+move[1])
            rope[i+1] = t
        pos.append(rope[-1])
            #print(delta,move)
    print(d,n,rope)
    #print(h,t)
print(len(set(pos)))
