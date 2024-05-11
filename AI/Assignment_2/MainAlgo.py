from BreadthFirstSearch import Breadth_First_Search
from UniformCostSearch import UniformCostSearch

locations = [
    "Bucharest", #0
    "Arad", #1
    "Craiova", #2
    "Drobeta", #3
    "Eforie", #4
    "Fagaras", #5
    "Giurgiu", #6
    "Hirsova", #7
    "Lasi", #8
    "Lugoj", #9
    "Mehadia", #10
    "Naemt", #11
    "Oradea", #12
    "Pitesti", #13
    "Rimnieu", #14
    "Sibiu", #15
    "Timisoara", #16
    "Urziceni", #17
    "Vaslui", #18
    "Zerind" #19
]
rows = 20
cols = 20
graph = [[0 for x in range(rows)] for y in range(cols)]

graph [0][17] = 85
graph [17][0] = 85

graph [0][6] = 90
graph [6][0] = 90

graph [0][13] = 101
graph [13][0] = 101

graph [0][5] = 211
graph [5][0] = 211

graph[8][11] = 87
graph[11][8] = 87

graph[8][18] = 92
graph[18][8] = 92

graph[18][17] = 142
graph[17][18] = 142

graph[17][7] = 98
graph[7][17] = 98

graph[7][4] = 86
graph[4][7] = 86

graph[12][19] = 71
graph[19][12] = 71

graph[12][15] = 151
graph[15][12] = 151

graph[1][19] = 75
graph[19][1] = 75

graph[1][15] = 140
graph[15][1] = 140

graph[1][16] = 118
graph[16][1] = 118

graph[16][9] = 111
graph[9][16] = 111

graph[9][10] = 70
graph[10][9] = 70

graph[10][3] = 75
graph[3][10] = 75

graph[3][2] = 120
graph[2][3] = 120

graph[2][13] = 138
graph[13][2] = 138

graph[2][14] = 146
graph[14][2] = 146

graph[13][14] = 97
graph[14][13] = 97

graph[15][14] = 80
graph[14][15] = 80

graph[15][5] = 99
graph[5][15] = 99

locations_heuristic = [0, 366, 160, 242, 161, 176, 77, 151, 226, 244, 241, 234, 380, 100, 193, 253, 329, 80, 199, 374]

# print(graph)
path = []
start = 11
end = 12
Breadth_First_Search(graph,rows, start, end, path)
# UniformCostSearch(graph, rows, start, end, path)
for i in range(path.__len__()):
    print(locations[path[i]], " ")