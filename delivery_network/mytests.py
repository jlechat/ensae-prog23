from graph import graph_from_file, graph_from_file_route
from random import randrange, choice
from time import perf_counter
from spanning_tree import UnionFind
from spanning_tree import Kruskal, path_spanning_tree

g = graph_from_file_route("input/network.2.in")
S=Kruskal(g)
print(path_spanning_tree(S,4,6))
