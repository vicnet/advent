import os

def read(file, input=None):
    path = os.path.dirname(os.path.abspath(file))
    lines = []
    if input is None:
        input = 'input'
    else:
        input = 'example' + str(input)
    with open(path+'/'+input, 'r') as f:
        for l in f:
            lines.append(l.strip())
    return lines
