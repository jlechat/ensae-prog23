from graph import Graph, graph_from_file, graph_from_file_route
from time import perf_counter
from random import randrange, seed, choice
seed(4)
data_path = "input/"
file_name = "routes.2.in"
g = graph_from_file_route(data_path + file_name)

it=1
temps_tot=0
liste=[l for l in g.graph.keys()]
for i in range(it) :
    a=choice(liste)
    b=choice(liste)
    time_begin=perf_counter()

    g.get_path_with_power(a, b, 10)

    time_stop=perf_counter()
    print("Il s'est écoulé : ", time_stop-time_begin, "secondes.")
    temps_tot+=time_stop-time_begin

print("Il s'est écoulé en moyenne : ", (time_stop-time_begin)/it, "secondes.")