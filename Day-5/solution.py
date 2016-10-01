import re

g1 = re.compile('(.*[aeiou].*){3,}')
g2 = re.compile('(\w)\\1')
bad = re.compile('ab|cd|pq|xy')

count = 0
for l in open("input.txt"):
    if not bad.search(l) and (g1.search(l) and g2.search(l)):
        count += 1

print(count)
