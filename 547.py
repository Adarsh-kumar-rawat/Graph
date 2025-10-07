class Solution:
    def DFS(self,i,adjMatrix, visited):
            visited[i]= True
            for x in range(0,len(adjMatrix)):
                if adjMatrix[i][x]==1 and not visited[x]:
                    self.DFS(x,adjMatrix,visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int: # type: ignore
        n = len(isConnected)
        visited = [False]*n
        ans= 0
        for i in range(n):
            if not visited[i]:
                self.DFS(i,isConnected,visited)
                ans +=1
        return ans

        #time Comp - O(e+v) edge + vertix