MAX = 1000000000000

def minDistance(dist, visited, size):
    min = MAX
    min_index = -1
    # Search not in shortest path
    for u in range(size):
        if (dist[u] < min and visited[u] == False):
            min = dist[u]
            min_index = u
    return min_index

def UniformCostSearch(graph, size, startNode, endNode, path):
    dist = [MAX] * size
    
    dist[startNode] = 0
    
    visited = [False] * size
    
    cost = 0

    lastNodeTraversed = startNode
    for count in range(size):
        x = minDistance(dist,visited, size)

        visited[x] = True

        path.append(x)

        cost += graph[x][lastNodeTraversed]
        lastNodeTraversed = x
        
        if x == endNode:
            break

        for y in range(size):
            if graph[x][y] > 0 and visited[y] == False and dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
    
    print("\n", cost, "\n")