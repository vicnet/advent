#!/usr/bin/env python3

file = open('input.txt', 'r')
lines = file.readlines()

l = lines[0].strip()
#l ='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
#print(l)
start = 0
for i in range(len(l)-14):
    s = l[i:i+14]
    uniq = True
    #print(s)
    for j in s:
        count = 0
        for k in s:
            if j==k: count += 1
        if count!=1:
            uniq = False
            break
    if uniq:
        start = i+14
        break
print(start)
