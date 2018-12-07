import re
from collections import defaultdict, Counter

coords = []

regex = re.compile("(\d+), (\d+)")

def get_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

with open("input.txt") as f:
    for s in f:
        x, y = regex.search(s).groups()
        coords.append((int(x), int(y)))

max_x = max(x[0] for x in coords)
max_y = max(x[1] for x in coords)
min_x = min(x[0] for x in coords)
min_y = min(x[1] for x in coords)

map = defaultdict(dict)
counter = Counter()
infinte = set()

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        distances = sorted((get_distance((x, y), p), idx) for idx, p in enumerate(coords))
        map[x][y] = sum(distance[0] for distance in distances)

        if distances[0][0] != distances[1][0]:
            counter.update([distances[0][1]])
        if x in (min_x, max_x) or y in (min_y, max_y):
            infinte.add(distances[0][1])

for x in counter.most_common():
    if x[0] not in infinte:
        print(x[1])
        break

area_size = 0
for x in map.values():
    for y in x.values():
        area_size += y < 10000

print(area_size)

