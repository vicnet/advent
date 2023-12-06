#!/usr/bin/env python3
import helper
import re

lines = helper.read(__file__)

sum = 0
for l in lines:
    nums = re.findall(r'\d', l)
    val = int(nums[0])*10 +  int(nums[-1])
    print(l, nums, val)
    sum += val
print(sum)
