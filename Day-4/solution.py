#!/usr/bin/env python

from hashlib import md5

i = 0
input = "yzbqklnj"

while not md5(bytes(input + str(i), 'utf-8')).hexdigest().startswith("00000"):
    i += 1

print(i)
