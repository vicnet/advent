#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

trees = []
for l in lines:
    l = l.strip()
    trees.append([{'h':int(t),'vis':False, 'see': [0]*4} for t in list(l)])
#print(trees)

def visible(trees):
    for row in trees:
        max = None
        for t in row:
            h,pres = t.values()
            if max is None:
                # edge
                t['vis'] = True
                max = h
                continue
            if h>max:
                # visible
                t['vis'] = True
                max = h
                continue
            # not visible
        #print(row)

def show(trees, vis=True):
    for row in trees:
        s = ''
        for t in row:
            if vis:
                s += str(t['h'])+str(t['vis'])[0]+' '
            else:
                s += str(t['h'])+'-'+str(t['see'])+' '
        print(s)

def seight(trees, pos):
    for row in trees:
        #print(row)
        for i,t in enumerate(row):
            look = row[i+1:]
            for l in look:
                t['see'][pos] += 1
                if t['h']<=l['h']:
                    break

#show(trees,False)
seight(trees, 0)
#show(trees,False)

#visible(trees)
#show()
#print()
for row in trees:
    row.reverse()
#visible(trees)
seight(trees, 1)
#show(trees,False)

ntrees = []
for i in range(len(trees[0])):
    row = []
    for stree in trees:
        row.append(stree[i])
    ntrees.append(row)
#show(ntrees)
#visible(ntrees)
seight(ntrees, 2)
#show(trees,False)

for row in ntrees:
    row.reverse()
#visible(ntrees)
seight(ntrees, 3)
#show(ntrees,False)

count = 0
max = 0
for row in trees:
    for t in row:
        if t['vis']:
            count += 1
        score = 1
        for s in t['see']:
            score *= s
        #print(t,score)
        if score>max:
            max = score
#print(count)
print(max)
