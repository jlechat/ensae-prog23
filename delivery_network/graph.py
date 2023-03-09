class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor1, p1, d1), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges.
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.nodes  : 
            self.nodes.append(node1)
            self.graph[node1]=[]
            self.nb_nodes+=1
        if node2 not in self.nodes : 
            self.nodes.append(node2)
            self.graph[node2]=[]
            self.nb_nodes+=1
        self.graph[node1]=self.graph[node1]+[[node2, power_min, dist]]
        self.graph[node2]=self.graph[node2]+[[node1, power_min, dist]]
        self.nb_edges+=1


    def get_path_with_power(self, src, dest, power): #complexité de O(n+m)
        import math
        visited = {node : False for node in self.nodes}
        distance = {node : math.inf for node in self.nodes}
        visited[src] = True
        distance[src] = 0
        k = src
        path = [src]
        while dest not in path : 
            min_dist = math.inf
            for node in self.graph[k] :
                new_dist = distance[k] + node[1]
                if not visited[node[0]]:
                    if new_dist < distance[node[0]] and node[2] <= power :
                        distance[node[0]] = new_dist
                    if distance[node[0]] < min_dist :
                        min_dist = distance[node[0]]
                        min_node = node[0]
            if min_dist != math.inf :
                visited[min_node] = True
                path.append(min_node)
                k = min_node
            else : return None      
        return "path : " + str(path) + ", distance : " + str(distance[dest])
"""
    def get_path_with_power(self, src, dest, power): #complexité de O(n+m)

        nodes_v={node : False for node in self.nodes} #dictionnaire qui permet de savoir si l'on est déjà passé par un point
        nodes_v[src] = True
        def parcours(node, chemin) :
            if node == dest:
                return chemin
            for i in self.graph[node] :
                k=i[0]
                k_power = i[1]
                if power >= k_power and not nodes_v[k]:
                    nodes_v[k]=True
                    return parcours(k, chemin+[k])
                if i == self.graph[node][-1] and chemin[-1] != src :
                    nodes_v[i[0]]=True
                    chemin.pop()
                    k = chemin[-1]
                    return parcours(k, chemin)
            return None

        return parcours(src, [src])
"""



    def connected_components(self) :
        """Méthode qui permet d'obtenir une liste contenant les éléments connectés entre eux.
        C'est à dire, les noeuds qui sont reliés entre eux.

        Returns:
            Liste: liste de liste des composants connectés.
        """
        l=[] #listes vides qui contiendra les listes de composants connectés
        nodes_v={node : False for node in self.nodes} #dictionnaire qui permet de savoir si l'on est déjà passé par un point

        def components(node) :
            comp=[node] #on initialise la liste avec le composant dont on veut connaitre ceux auxquels il est connecté
            for i in self.graph[node] : #on parcourt tous les voisins du noeux "node"
                k=i[0]
                if not nodes_v[k] :
                    nodes_v[k]=True #on indique que l'on vient de parcourir ce noeud
                    comp+=components(k) #on utilise la récursivité pour obternir les voisins des voisins... et in fine cela retourne tous les élements connectés
            return comp
        
        for k in self.nodes : #on parcourt tous les noeuds
            if not nodes_v[k] : l.append(components(k)) #si le noeud n'a pas été parcouru on ajoute la liste de ses composants connectés

        return l



    def connected_components_set(self):
        """
        The result should be a set of frozensets (one per component), 
        For instance, for network01.in: {frozenset({1, 2, 3}), frozenset({4, 5, 6, 7})}
        """
        return set(map(frozenset, self.connected_components()))
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        """
        nodes_v={node : False for node in self.nodes} #dictionnaire qui permet de savoir si l'on est déjà passé par un point
        nodes_v[src] = True
        def parcours(node, chemin, p) :
            if node == dest:
                return chemin, p
            for i in self.graph[node] :
                k=i[0]
                k_power = i[1]
                if not nodes_v[k]:
                    nodes_v[k]=True
                    if k_power>p : p=k_power
                    return parcours(k, chemin+[k], p)
            return None

        return parcours(src, [src],0)
        """
        a = 0
        b = 1
        def dicho(a, b) : #on utilise la méthode de la dichotomie
            while b-a > 0.1 : #on fixe le taux d'arret à 0.1
                if self.get_path_with_power(src, dest, (a+b)/2) != None: #si la puissance est trop grande on ramène b au milieu du segment [a,b]
                    b = (a+b)/2
                else : #si la puissance est assez grande on ramène a au milieu du segment [a,b]
                    a = (a+b)/2
                dicho(a, b) #on utilise la récursivité pour réduire la taille de notre interval
            return self.get_path_with_power(src, dest, b), b

        while self.get_path_with_power(src, dest, b) == None :
            b = 2*b #on multiplie b par 2 jusqu'a temps que l'on puisse réaliser le chemin avec la puissance b
        return dicho(a, b)

def graph_from_file(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class.

    The file should have the following format: 
        The first line of the file is 'n m'
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    f=open(filename)
    ligne=f.readline().split()
    nb_node=int(ligne[0])
    nb_edge=int(ligne[1])
    nodes=[i for i in range(1, nb_node+1)]
    G=Graph(nodes)
    for i in range(nb_edge) :
        ligne=f.readline().split()
        node1=int(ligne[0])
        node2=int(ligne[1])
        power_min=int(ligne[2])
        if len(ligne)==3 : G.add_edge(node1, node2, power_min)
        else : 
            dist=int(ligne[3])
            G.add_edge(node1, node2, power_min, dist)
    return G

def graph_from_file_route(filename):
    """
    Reads a text file and returns the graph as an object of the Graph class, for files routes.

    The file should have the following format: 
        The first line of the file is 'n' the number of edges
        The next m lines have 'node1 node2 power_min dist' or 'node1 node2 power_min' (if dist is missing, it will be set to 1 by default)
        The nodes (node1, node2) should be named 1..n
        All values are integers.

    Parameters: 
    -----------
    filename: str
        The name of the file

    Outputs: 
    -----------
    G: Graph
        An object of the class Graph with the graph from file_name.
    """
    f=open(filename)
    ligne=f.readline().split()
    nb_node=int(ligne[0])
    nb_edge=int(ligne[0])
    nodes=[i for i in range(1, nb_node+1)]
    G=Graph(nodes)
    for i in range(nb_edge) :
        ligne=f.readline().split()
        node1=int(ligne[0])
        node2=int(ligne[1])
        power_min=int(ligne[2])
        if len(ligne)==3 : G.add_edge(node1, node2, power_min)
        else : 
            dist=int(ligne[3])
            G.add_edge(node1, node2, power_min, dist)
    G.graph={k: v for k, v in G.graph.items() if v != []}
    G.nb_nodes=len(G.graph)
    return G
