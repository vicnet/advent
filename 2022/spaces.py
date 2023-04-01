#!/usr/bin/env python3

file = open('input.txt', 'r')
lines = file.readlines()
#lines=[
#'2-4,6-8',
#'2-3,4-5',
#'5-7,7-9',
#'2-8,3-7',
#'6-6,4-6',
#'2-6,4-8',
#]
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

total = 0
for l in lines:
    l = l.strip()
    elves = l.split(',')
    #print(elves)
    couple = []
    for elve in elves:
        spaces = elve.split('-')
        #print(' =>',spaces)
        spaces = range(int(spaces[0]),int(spaces[1])+1)
        spaces = list(spaces)
        #print(' =>',spaces)
        couple.append(spaces)
    #print(couple)
    inter = intersection(couple[0],couple[1])
    #if inter in couple:
    if inter:
        total += 1
    #print(inter, total)
print(total)
