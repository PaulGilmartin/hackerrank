def Dijkstra(Graph, source, edge_lengths):
    dist_dic, unvisited = {}, set(Graph.keys())
    for vertex in unvisited:
        dist_dic[vertex] = float("inf")

    dist_dic[source] = 0

    while unvisited:

        current = min(unvisited, key=dist_dic.get)
        for neighbour in Graph[current]:
            if neighbour in unvisited:
                alt = dist_dic[current] + edge_lengths[(current, neighbour)]
                if alt < dist_dic[neighbour]:
                    dist_dic[neighbour] = alt
        unvisited = unvisited - {current}

    for node in dist_dic.keys():  #only need this for hackerrank problem - wants -1 instead of standard infinity
        if dist_dic[node] == float("inf"):
            dist_dic[node] = -1
    del dist_dic[source]
    return dist_dic




T = int(input())
for test in range(T):
    nums = input().split()
    N, M = int(nums[0]), int(nums[1])
    vertices, edges = list(range(1, N+1)), []
    Graph = {v: set() for v in vertices}
    lengths = {}
    for line in range(M):
        edge = list(map(int, input().split()))
        Graph[edge[0]].add(edge[1])
        Graph[edge[1]].add(edge[0])
        length = edge[2]
        lengths[(edge[0], edge[1])] = min(lengths.get((edge[0], edge[1]), float("inf")), length)
        lengths[(edge[1], edge[0])] = min(lengths.get((edge[1], edge[0]), float("inf")), length)

    start = int(input())
    #print(lengths)

    print(*Dijkstra(Graph, start, lengths).values(), sep=" ")
