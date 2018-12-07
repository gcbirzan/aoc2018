import time

with open("input.txt") as f:
    s = f.read().strip()


def react(s):
    s = list(map(ord, s))
    current = 1
    prevs = [0]
    length = len(s)
    while current < length:
        prev = prevs[-1]
        if s[prev] - s[current] == 32 or s[prev] - s[current] == -32:
            current += 1
            prevs.pop()
            if not prevs:
                prevs = [current]
                current += 1
        else:
            prevs.append(current)
            current += 1

    return prevs


start_t = time.time()

orig_s = ''.join(s[x] for x in react(s))
print(len(orig_s))
lengths = []
for x in range(0, 26):
    s = orig_s
    s = s.replace(chr(x + 65), '')
    s = s.replace(chr(x + 97), '')
    lengths.append(len(react(s)))

print(min(lengths))

print(time.time() - start_t)