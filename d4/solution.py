import datetime
import re
from collections import defaultdict, Counter


line_regex = re.compile(r"\[(.*)\] (.*)")
guard_regex = re.compile(r'Guard #(\d+) begins shift')
timestamps = []
actions = {}

with open("input.txt") as f:
    for s in f:
        ts, action = line_regex.search(s).groups()
        ts = datetime.datetime.strptime(ts, "%Y-%m-%d %H:%M")
        timestamps.append(ts)
        if 'Guard' in action:
            action = int(guard_regex.search(action).group(1))
        elif 'falls' in action:
            action = -1
        else:
            action = -2
        actions[ts] = action

guards_sleep_counter = defaultdict(Counter)

timestamps.sort()
current_guard = None
asleep_ts = None

for ts in timestamps:
    action = actions[ts]
    if action > 0:
        current_guard = action
    elif action == -1:
        asleep_ts = ts
    else:
        guards_sleep_counter[current_guard].update(range(asleep_ts.minute, ts.minute))

most_sleepy = (
    (guard, sum(sleep.values()), sleep.most_common(1)[0][0])
    for guard, sleep in guards_sleep_counter.items()
)
guard, max_sleep, minute = max(most_sleepy, key=lambda x: x[1])
print(guard * minute)

most_asleep = (
    (guard, sleep.most_common(1)[0])
    for guard, sleep in guards_sleep_counter.items()
)
guard, sleep = max(most_asleep, key=lambda x: x[1][1])
print(guard * sleep[0])
