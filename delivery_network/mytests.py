from graph import graph_from_file, graph_from_file_route
from random import randrange, choice
from time import perf_counter
"""
g = graph_from_file("input/network.04.in")
print(g.graph)"""

g = graph_from_file_route("input/routes.2.in")

liste=[l for l in g.graph.keys()]
a=choice(liste)
b=choice(liste)

#A faire ! Changer directement le nombres de noeuds pour optimiser !!