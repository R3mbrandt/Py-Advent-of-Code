#!/usr/bin/env python

directions = open('input.txt').read()

x, y = 0, 0
houses = {(x, y)}

for d in directions:
    if d == '^':
        y += 1
    elif d == 'v':
        y -= 1
    elif d == '>':
        x += 1
    elif d == '<':
        x -= 1
    houses.add((x, y))

print(houses)
print(len(houses))
