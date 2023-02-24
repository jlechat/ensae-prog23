from graph import *

g = graph_from_file("input/network.02.in")
print(g)
print(g.min_power(1, 3))

from graphviz import Source

s = Source(g, filename="test.gv", format="png")
s.view()