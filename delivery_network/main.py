from graph import Graph, graph_from_file
from time import perf_counter
from random import randrange, seed
random.seed(4)
data_path = "input/"
file_name = "routes.1.in"
g = graph_from_file(data_path + file_name)

it=5
temps_tot=0
for i in range(it) :
    a=randrange(min(g.graph.keys()), max(g.graph.keys()))
    time_begin=perf_counter()

    g.get_path_with_power(src, dest, power)

    time_stop=perf_counter()
    print("Il s'est écoulé : ", time_stop-time_begin, "secondes.")
    temps_tot+=time_stop-time_begin

print("Il s'est écoulé en moyenne : ", (time_stop-time_begin)/it, "secondes.")