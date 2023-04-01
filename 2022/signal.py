#!/usr/bin/env python3

from pprint import pprint

file = open('input.txt', 'r')
lines = file.readlines()

X = 1
cycles = [X]
for l in lines:
    l = l.strip()
    if l=='noop':
        cycles.append(X)
        #print(len(cycles)-1,l,X)
    else:
        i,v = l.split()
        #print(i,v)
        cycles.append(X)
        #print(len(cycles)-1,l,X)
        X += int(v)
        cycles.append(X)
        #print(len(cycles)-1,l,X)

#print(cycles[20],cycles[60],cycles[100],cycles[140],cycles[180],cycles[220])
total = 0
for i in range(20,260,40):
    power = i*cycles[i-1]
    total += power
    #print(i,cycles[i], power)
#print(total)

print(cycles[1:5])

for l in range(6):
    line = ''
    for i in range(40):
        sprite = cycles[i + l*40]
        if i>=sprite-1 and i<=sprite+1:
            line += '#'
        else:
            line += '.'
        #print(i,sprite,line)
    print(line)
