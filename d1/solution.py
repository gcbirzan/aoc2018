import itertools

frequency = 0
reached_frequencies = {0}
f_deltas = []
idx = 0

with open("input.txt") as f:
    for line in f:
        idx += 1
        f_delta = int(line.strip())
        frequency += f_delta
        f_deltas.append(f_delta)
print(frequency)
frequency = 0
idx = 0
for f_delta in itertools.cycle(f_deltas):
    idx += 1
    frequency += f_delta
    if frequency in reached_frequencies:
        print(frequency)
        break
    reached_frequencies.add(frequency)
