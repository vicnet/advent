#!/usr/bin/env python3

from pprint import pprint
from collections import OrderedDict

file = open('input.txt', 'r')
lines = file.readlines()

for l in lines:
    l = l[:-1]
    print('"',l,'"')
