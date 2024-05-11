
def Breadth_First_Search(graph, length, startNode, endNode,  path):
    visited = [False] * length
    queue = []

    queue.append(startNode)
    visited[startNode] = True
    cost = 0
    last = startNode
    start = startNode
    while queue:
        last = start
        start = queue.pop(0)
        path.append(start)
        cost += graph[start][last]
        if start == endNode:
            break
        for i in range(length):
            if graph[start][i] != 0 and (not visited[i]):
                queue.append(i)
                visited[i] = True
    print("\n", cost, "\n")
