"""
Given a weighted undirected graph, we need to find the spanning tree of minimal overall
weight, i.e., a subtree which contains every node of the graph whose sum of weights of 
edges is minimal over all such trees.
"""

class TreeFinder(object):
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges #edges are a triple: (v, w, weight v-w)
        self.withoutweights = [set(e[:2]) for e in self.edges]    
        self.weights = self.weightsDict() #dict with key, value pairs (v, w): min weight between v and w
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
        #C = {v: float("inf") for v in self.nodes}
        #E = {v: False for v in self.nodes}
        while queue:
            min_weight = float("inf")
            for node in queue:
                neighbours = {v for v in tree_nodes if {node, v} in self.withoutweights}
                if neighbours:
                    #print "edges", [(v, node) for v in neighbours]
                    cheapest_edge = min([(v, node) for v in neighbours], key=lambda x:self.weights[x])
                    weight = self.weights[(v, node)]
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
        return tree_edges
            #C[best_node] = min_weight
            #E[best_node] = best_edge





        


    
                                                                
