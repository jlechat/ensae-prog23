from graph import graph_from_file, graph_from_file_route
from random import randrange, choice
from time import perf_counter
from spanning_tree import UnionFind
from spanning_tree import Kruskal, path_spanning_tree

g = graph_from_file("input/network.02.in")
S = Kruskal(g)
print(g)
print(S)
print(path_spanning_tree(S,1,2))
