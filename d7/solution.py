import re

import networkx as nx

extra_time = 60
workers = 5

regex = re.compile(r"Step ([^ ]+) must be finished before step ([^ ]+) can begin.")

graph = nx.DiGraph()

with open("input.txt") as f:
    for s in f:
        x, y = regex.search(s).groups()
        graph.add_edge(x, y)

print(''.join(nx.lexicographical_topological_sort(graph)))

workers_state = {x: (1, None) for x in range(workers)}
done = set()
work_times = {node: ord(node) - 64 + extra_time for node in graph.nodes}

reachable_nodes = set(x[0] for x in graph.in_degree if x[1] == 0)
nodes_left = set(graph.nodes) - reachable_nodes


def get_time():
    second = 0

    while True:
        for worker, state in workers_state.items():
            if state[1] is None:
                continue
            if state[0] == 1:
                if state[1]:
                    done.add(state[1])
                    for node in list(nodes_left):
                        if all(x in done for x in graph.predecessors(node)):
                            reachable_nodes.add(node)
                            nodes_left.remove(node)
                    workers_state[worker] = (0, None)
            else:
                workers_state[worker] = (state[0] - 1, state[1])

        for worker, state in workers_state.items():
            if state[1] is None:
                if reachable_nodes:
                    node = sorted(reachable_nodes)[0]
                    reachable_nodes.remove(node)
                    workers_state[worker] = (work_times[node], node)

        if len(done) == len(graph.nodes):
            return second
        second += 1


print(get_time())
