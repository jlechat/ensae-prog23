from graph import graph_from_file, graph_from_file_route


g = graph_from_file("input/network.04.in")
print(g)
print(g.min_power(1, 4)[1])

