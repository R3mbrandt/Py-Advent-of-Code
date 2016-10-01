import re
from itertools import permutations

c = re.compile("(\w+) to (\w+)")
d = re.compile("(\d+)")

cities = set()
distances = dict()
routes = dict()

for line in open("input.txt"):
    (c1, c2) = c.search(line).groups()
    distance = d.search(line).group(0)
    distances[(c1, c2)] = distances[(c2, c1)] = distance
    cities.add(c1)
    cities.add(c2)

for p in permutations(cities):
    dist = 0
    for i in range(0, len(p) - 1):
        dist += int(distances[(p[i], p[i + 1])])
    routes[p] = dist

print(routes[max(routes, key=routes.get)])
