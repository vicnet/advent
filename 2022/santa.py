#!/usr/bin/env python3

file = open('input.txt', 'r')
lines = file.readlines()
#lines=[
#'A Y',
#'B X',
#'C Z',
#]

he_map = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors',
    }
me_map = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z': 'Scissors',
    }
sel_points = {
    'Rock': 1,
    'Paper': 2,
    'Scissors': 3,
    }
out_points = {
    'win': 6,
    'draw': 3,
    'lost': 0,
    }
winner = [
    ('Rock','Scissors'),
    ('Scissors','Paper'),
    ('Paper','Rock'),
]

table = {}
for he in sel_points.keys():
    for me in sel_points.keys():
        match = (he,me)
        table[match] = sel_points[me]
        if match in winner:
            table[match] += out_points['lost']
        elif tuple(reversed(match)) in winner:
            table[match] += out_points['win']
        else:
            table[match] += out_points['draw']
#print(table)

def phase1():
    points = 0
    for l in lines:
        l = l.strip()
        he,me = l.split(' ')[:2]
        #print(he,me)
        he = he_map[he]
        me = me_map[me]
        #print(he,me, table[(he,me)])
        points += table[(he,me)]
    print(points)

me2_map = {
    'X': 'lost',
    'Y': 'draw',
    'Z': 'win',
    }

points = 0
for l in lines:
    l = l.strip()
    he,me = l.split(' ')[:2]
    print(he,me)
    he = he_map[he]
    # indirection
    me = me2_map[me]
    if me=='draw':
        me = he
    elif me=='win':
        for win,lost in winner:
            if lost==he:
                me = win
                break
    else: # lost
        for win,lost in winner:
            if win==he:
                me = lost
                break
    print(he,me, table[(he,me)])
    points += table[(he,me)]
print(points)
