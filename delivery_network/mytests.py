from graph import *

g = graph_from_file("input/network.04.in")
print(g)
print(g.get_path_with_power(1, 4, 11))
print(g.graph[3])
print(g.min_power(1, 3))
print(g.get_path_with_power(2, 4, 6))