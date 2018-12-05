data = []
with open("input.txt") as f:
    for s in f:
        data.append(s.strip())

for idx, s1 in enumerate(data):
    for s2 in data[idx+1:]:
        diff = 0
        for s in zip(s1, s2):
            diff += s[0] != s[1]
        if diff == 1:
            print(''.join(s[0] for s in zip(s1, s2) if s[0] == s[1]))
            break
