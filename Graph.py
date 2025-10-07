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

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def pop(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the item at the front without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def size(self):
        """Return the number of items in the queue."""
        return len(self.items)

    def __str__(self):
        """String representation of the queue."""
        return "Queue: " + str(self.items)
    
