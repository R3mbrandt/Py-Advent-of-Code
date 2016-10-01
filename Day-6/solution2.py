import re

lights = [[0 for x in range(1000)] for y in range(1000)]

what = re.compile('(\w+) \d')
nums = re.compile('(\d+)')

for line in open("input.txt"):
    switch = what.search(line).group(1)
    (startx, starty, endx, endy) = [int(x) for x in nums.findall(line)]

    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            if switch == "on":
                lights[x][y] += 1
            elif switch == "off":
                if lights[x][y] > 0:
                    lights[x][y] -= 1
            elif switch == "toggle":
                lights[x][y] += 2

summe = 0
for y in lights:
    for x in y:
        summe += x

print(summe)
