# !/usr/bin/env python

from functools import reduce
from operator import mul

total = 0

for line in open("input.txt"):
    (l, b, h) = [int(x) for x in line.split('x')]
    extra = reduce(mul, sorted([l, b, h])[:2])
    total += extra + 2 * (l * b + l * h + b * h)

print(total)
