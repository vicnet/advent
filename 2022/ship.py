count = None
old = 0
file = open('input.txt', 'r')
lines = file.readlines()
lines=[
'199',
'200',
'208',
'210',
'200',
'207',
'240',
'269',
'260',
'263',
]

for l in lines:
    if l is None: break
    val = int(l)
    print(old,val,count)
    if count is None:
        count = 0
        old = val
        continue
    if val>old: count += 1
    old = val
    #print(val)
print(len(lines), count)
