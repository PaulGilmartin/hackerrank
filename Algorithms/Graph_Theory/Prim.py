"""
Given a weighted undirected graph, we need to find the spanning tree of minimal overall
weight, i.e., a subtree which contains every node of the graph whose sum of weights of 
edges is minimal over all such trees.
"""

class TreeFinder(object):
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges #edges are a triple: (v, w, weight v-w)
        self.weights = self.weightsDict() #dict with key, value pairs (v, w): min weight between v and w
        self.withoutweights = self.weights.keys()
        self.graphDict = self.adjacencyListBuilder()[0]

    def __str__(self):
        return edges
    
    def adjacencyListBuilder(self):
        graph_dict = {v: set() for v in self.nodes}
        weights = {}
        for edge in self.edges:
            graph_dict[edge[0]].add(edge[1])
            graph_dict[edge[1]].add(edge[0])
            length = edge[2]
            weights[(edge[0], edge[1])] = min(weights.get((edge[0], edge[1]),
                                                                    float("inf")), length)
            weights[(edge[1], edge[0])] = min(weights.get((edge[1], edge[0]),
                                                                    float("inf")), length)
        return graph_dict, weights

    def weightsDict(self):
        return self.adjacencyListBuilder()[1]

    def minSpanningTree(self, start):
        queue = self.nodes[:]
        queue.remove(start)
        tree_nodes = [start]
        tree_edges = []
        total_weight = 0
        while queue:
            min_weight = float("inf")
            for node in queue:
                neighbours = {v for v in tree_nodes if v in self.graphDict[node]}
                if neighbours:
                    cheapest_edge = min([(v, node) for v in neighbours], key=lambda x:self.weights[x])
                    weight = self.weights[cheapest_edge]
                    if weight < min_weight:
                        best_node = node
                        min_weight = weight
                        best_edge = cheapest_edge
                else:
                    continue
            queue.remove(best_node)
            tree_nodes.append(best_node)
            tree_edges.append(best_edge)
            total_weight += min_weight
        return total_weight


    def minSpanningTree2(self, start):
        total_weight = 0
        queue = self.nodes[:]
        queue.remove(start)
        edges_left = [set(e[:2]) for e in self.edges]
        tree_nodes = {start}
        while queue:
            possible_edges = [e for e in edges_left if bool(e&tree_nodes) and bool(e&set(queue))]
            cheapest_edge = min(possible_edges, key=lambda x: self.weights[tuple(x)])
            total_weight += self.weights[tuple(cheapest_edge)]
            edges_left.remove(cheapest_edge)
            for _ in cheapest_edge:
                tree_nodes.add(_)
                try:
                    queue.remove(_)
                except ValueError:
                    pass
        return total_weight






        


    
                                                                
