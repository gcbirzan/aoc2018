import re

claims = {}
regex = re.compile("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")
with open("input.txt") as f:
    for s in f:
        idx, x, y, xd, yd = regex.search(s).groups()
        claims[idx] = ((int(x), int(y)), (int(xd), int(yd)))

fabric = [[[] for y in range(1000)] for x in range(1000)]
overlapping = set()
for claim_id, claim in claims.items():
    for x in range(claim[0][0], claim[1][0] + claim[0][0]):
        for y in range(claim[0][1], claim[1][1] + claim[0][1]):
            fabric[x][y].append(claim_id)

total = 0
for x in fabric:
    for y in x:
        if len(y) > 1:
            overlapping = overlapping.union(y)
            total += 1

print(total)
print(set(claims) - overlapping)
