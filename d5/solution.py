import time

with open("input.txt") as f:
    s = f.read().strip()


def get_len(s):
    current = 1
    prevs = [0]
    while current < len(s):
        prev = prevs[-1]
        if abs(ord(s[prev]) - ord(s[current])) == 32:
            current += 1
            prevs.pop()
            if not prevs:
                prevs = [current]
                current += 1
        else:
            prevs.append(current)
            current += 1

    return len(prevs)


start_t = time.time()

print(get_len(s))

orig_s = s
lengths = []
for x in range(0, 26):
    s = orig_s
    s = s.replace(chr(x + 65), '')
    s = s.replace(chr(x + 97), '')
    lengths.append(get_len(s))

print(min(lengths))

print(time.time() - start_t)