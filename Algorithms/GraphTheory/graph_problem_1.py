def BFS_level(graph, start):
    visited, queue = {start}, deque([start])
    level_dic = {}
    while queue:
        current = queue.popleft()
        for neighbour in graph[current]:
            if neighbour not in visited:
                level_dic[neighbour] = level_dic.get(current, 0) + 6
                queue.append(neighbour)
                visited.add(neighbour)
    for node in set(vertices) - visited:
        level_dic[node] = -1
    return level_dic



T = int(input())
for test in range(T):
    nums = input().split()
    N, M = int(nums[0]), int(nums[1])
    vertices, edges = list(range(1, N+1)), []
    Graph = {v: set() for v in vertices}
    for line in range(M):
        edge = list(map(int, input().split()))
        Graph[edge[0]].add(edge[1])
        Graph[edge[1]].add(edge[0])
    start = int(input())

    print(*BFS_level(Graph, start).values(), sep=" ")
