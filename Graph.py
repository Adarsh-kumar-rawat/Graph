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


# TRAVERSAL MEDIUM 

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
    
#BFS
q = Queue()
visited = [False]*v
ans = []

q.push(0)
visited[0]=True
ans.append(0)

while q.size()>0:
    front = q.pop()
    for x in adjList[front]:
        if not visited[x]:
            q.push(x)
            visited[x]=True
            ans.append(x)
print(ans)

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top item from the stack."""
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Return the top item without removing it."""
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def size(self):
        """Return the number of items in the stack."""
        return len(self.items)

    def __str__(self):
        """String representation of the stack."""
        return "Stack(top -> bottom): " + str(self.items[::-1])
    
#DFS
q = Stack()
visited = [False]*v
ans = []

q.push(0)
visited[0]=True
ans.append(0)

while q.size()>0:
    front = q.pop()
    for x in adjList[front]:
        if not visited[x]:
            q.push(x)
            visited[x]=True
            ans.append(x)
print(ans)