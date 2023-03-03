from graph import *
from random import randrange

g = graph_from_file("input/network.04.in")
print(g)

a=randrange(min(g.graph.keys()), max(g.graph.keys()))
print(a, g.graph.keys(), min(g.graph.keys()), max(g.graph.keys()))