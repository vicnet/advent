#!/usr/bin/env python3

from pprint import pprint

lines = [
'$ cd /',
'$ ls',
'dir a',
'14848514 b.txt',
'8504156 c.dat',
'dir d',
'$ cd a',
'$ ls',
'dir e',
'29116 f',
'2557 g',
'62596 h.lst',
'$ cd e',
'$ ls',
'584 i',
'$ cd ..',
'$ cd ..',
'$ cd d',
'$ ls',
'4060174 j',
'8033020 d.log',
'5626152 d.ext',
'7214296 k',
]
file = open('input.txt', 'r')
lines = file.readlines()

base = {}
stack = [ base ]
for l in lines:
    l = l.strip()
    if '$'==l[0]:
        # commande
        if 'cd'==l[2:4]:
            cmd = l.split(' ')
            rep = cmd[2]
            if rep=='/':
                stack = [ base ]
            elif rep=='..':
                stack.pop()
            else:
                cur = stack[-1]
                new = cur[rep]
                stack.append(new)
        elif 'ls'==l[2:4]:
            pass
        else:
            print('cmd inconnue')
        continue
    if 'dir'==l[0:3]:
        # dir
        ls = l.split(' ')
        rep = ls[1]
        cur = stack[-1]
        cur[rep] = { }
        continue
    # fichier
    ls = l.split(' ')
    size = int(ls[0])
    name = ls[1]
    cur = stack[-1]
    cur[name] = size
    #print(name,size)
#pprint(base)

smax = 0

def taille(d):
    global smax
    total = 0
    for name,obj in d.items():
        if isinstance(obj,int):
            size = obj
            #print('file', name,obj)
        else:
            size = taille(obj)
            #print('dir', name, size)
            if size<=100000:
                smax += size
        total += size
    return total
#print(smax)

dirs = []
def fichiers(d):
    global dirs
    total = 0
    for name,obj in d.items():
        #if name=='fpj':pprint(obj)
        if isinstance(obj,int):
            size = obj
        else:
            size = fichiers(obj)
            #if name in dirs:
                #print(name,'deja existan !!!')
            dirs.append(size)
        total += size
    return total

disk = 70000000
minu = 30000000
total = fichiers(base)
#print(dirs)
left = disk-total
tofound = minu-left
print('==> left',left,' must found',tofound)
mins = None
for size in dirs:
    if size>=tofound:
        print(size, left+size, size>=tofound)
        if mins is None or size<mins:
            mins = size
            #print(name,left+size,mins)
print(mins)
