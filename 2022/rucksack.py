#!/usr/bin/env python3

file = open('input.txt', 'r')
lines = file.readlines()
#lines=[
#'vJrwpWtwJgWrhcsFMMfFFhFp',
#'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
#'PmmdzqPrVvPwwTWBwg',
#'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
#'ttgJtRGJQctTZtZT',
#'CrZsJsPPZsGzwwsLwLmpwMDw',
#]

import string
piorities = {}
for i,letter in enumerate(string.ascii_lowercase+string.ascii_uppercase):
    piorities[letter] = i+1
#print(piorities)

def part1(l):
    lg = len(l)
    if lg%2!=0: print('pas divisible')
    first = l[:-int(lg/2)]
    last = l[int(lg/2):]
    #print(first,last)
    found = None
    for item in first:
        if item in last:
            if found is not None:
                if found!=item:
                    print('deux differents !')
            else:
                found = item
                #print('- found',item)
    return found

total = 0
elves=['']*3
for i,l in enumerate(lines):
    l = l.strip()
    #found = part1(l)
    found = None
    elves[i%3] = l
    if i%3!=2: continue
    #print(elves)
    for item in elves[0]:
        if item in elves[1] and item in elves[2]:
            if found is not None:
                if found!=item:
                    print('deux differents !')
            else:
                found = item
                #print('- found',item)
    if found is None:
        print('not found')
        continue
    prio = piorities[found]
    total += prio
print(total)
