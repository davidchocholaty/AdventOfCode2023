# The code is taken over from the following source:
# https://github.com/hyper-neutrino/advent-of-code/blob/184ef265ce5f5cab0c3115fd4cf343115973506e/2023/day25.py

import networkx as nx

g = nx.Graph()

for line in open(0):
    left, right = line.split(":")
    for node in right.strip().split():
        g.add_edge(left, node)
        g.add_edge(node, left)

g.remove_edges_from(nx.minimum_edge_cut(g))
a, b = nx.connected_components(g)

print(len(a) * len(b))