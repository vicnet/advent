#!/usr/bin/env python3

file = open('input.txt', 'r')
lines = file.readlines()
lines=[
'A Y',
'B X',
'C Z',
]

he_map = {
    'A': 'Rock',
    'B': 'Paper',
    'C', 'Scissors',
    }
me_map = {
    'X': 'Rock',
    'Y': 'Paper',
    'Z', 'Scissors',
    }
sel_points = {
    'Rock': 1
    'Paper': 2
    'Scissors': 3
    }
out_points = {
    'win': 6,
    'draw': 3,
    'lost': 0
    }
winner = [
    ('Rock','Scissors'),
    ('Scissors','Paper'),
    ('Paper','Rock')
]

table = {}
for he in sel_points.keys():
    for me in sel_points.keys():
        match = (he,me)
        if match in winner:
            table[match] = out_points['lost']
        elif reversed(match) in winner:
            table[match] = out_points['win']
        else:
            table[match] = out_points['draw']
print(table)
points = 0
for l in lines:
    he,me = l.split(' ')[:2]
    print(he,me)
    
