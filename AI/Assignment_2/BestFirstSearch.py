
def BestFirstSearch(graph, size, startNode, endNode, path, heuristic):
    queue = []    
    visited = [False] * size
    queue.append(startNode)

    while queue:
        x = queue.pop()
        visited[x] = True
        if x == endNode:
            break
        min = 100000
        for z in range(size):
            for y in range(size):
                if graph[x][y] and visited[y] == False:
                    if heuristic[y] < min:
                        min = heuristic[y]
            if (not (min == 100000)):
                visited[y] = True
                queue.append(y)