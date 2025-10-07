v = 6
e = 7
sett = [(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]

# ADJACENCY LIST 
adjList = []

for i in range(v):
    adjList.append([])

for edge in sett:
    x = edge[0]
    y = edge[1]
    adjList[x].append(y)
    adjList[y].append(x)

for i in range(v):
    print(i ,"->",adjList[i])


# ADJ MATRIX
adjMatrix = []

for i in range(v):
    adjMatrix.append([0]*v)

for edge in sett:
    x = edge[0]
    y = edge[1]
    adjMatrix[x][y] =1 
    adjMatrix[y][x] =1
    print(x,y) 

for i in adjMatrix:
    print(i)