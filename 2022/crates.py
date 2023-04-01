#!/usr/bin/env python3

file = open('input.txt', 'r')
lines = file.readlines()
#lines=[
#'    [D]    ',
#'[N] [C]    ',
#'[Z] [M] [P]',
#' 1   2   3 ',
#'',
#'move 1 from 2 to 1',
#'move 3 from 1 to 3',
#'move 2 from 2 to 1',
#'move 1 from 1 to 2',
#]

n = int((len(lines[0])+1)/4)
stacks = [ ]
for i in range(n):
    stacks.append([])
for l in lines:
    if '1' in l:
        break
    for i in range(n):
        letter = l[i*4+1]
        if letter==' ': continue
        stacks[i].append(letter)
    #print(l)
for i in range(n):
    stacks[i].reverse()
#print(stacks)

moves = []
found = False
for l in lines:
    l = l.strip()
    if not found:
        if l!='': continue
        found = True
        continue
    move = l.split(' ')
    move = (move[1],move[3],move[5])
    #print(move)
    moves.append([int(i) for i in move])
    #print(move)
#print(moves)

for move in moves:
    #print(stacks)
    #print(move)
    n = move[0]
    sfrom = stacks[move[1]-1]
    sto = stacks[move[2]-1]
    #for i in range(n):
        #item = stacks[move[1]-1].pop()
        #stacks[move[2]-1].append(item)
    items = sfrom[-n:]
    #print('   ',items)
    del sfrom[-n:]
    sto += items
#print(stacks)

msg = ''
for stack in stacks:
    msg += stack[-1]
print(msg)
