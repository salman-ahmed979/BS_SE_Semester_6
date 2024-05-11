count = 0

def DLS(graph, size, src, target, maxDepth):
  
        if src == target : return True
  
        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0 : return False
  
        # Recur for all the vertices adjacent to this vertex
        for i in range(size):
            if graph[src][i]:
                count += graph[src][i]

                if(DLS(graph, size, i, target, maxDepth-1)):
                    return True
        return False

def IterativeDepeeningDepthFirstSearch(graph, size, startNode, endNode, x):
    
    for i in range(size):
        if DLS(graph, size, startNode, endNode, i):
            return True
    return False