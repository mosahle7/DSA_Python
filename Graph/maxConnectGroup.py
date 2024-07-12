from typing import List
class DisjointSet:
    def __init__(self,n):
        self.parent = list(range(n*n))
        self.size = [1]*(n*n)

    def find(self,x):
        if self.parent[x]!=x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootX=self.find(x)
        rootY=self.find(y)

        if rootX!=rootY:
            if self.size[rootX] > self.size[rootY]:
                self.parent[rootY] = rootX
                self.size[rootX]+=self.size[rootY]
            elif self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY]+=self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]

class Solution:
    def MaxConnection(self, grid : List[List[int]]) -> int:
        n = len(grid)
        ds = DisjointSet(n)

        dr = [-1,0,1,0]
        dc = [0,1,0,-1]

        for i in range(n):
            for j in range(n):

                if grid[i][j]==0: continue

                for k in range(4):
                    nrow = i+dr[k]
                    ncol = j+dc[k]

                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                        node = i*n+j
                        adjNode = nrow*n+ncol

                        ds.union(node, adjNode)
        
        ans=0
        for i in range(n):
            for j in range(n):
                if grid[i][j]==1: continue
                
                s=set()
                for k in range(4):
                    nrow = i+dr[k]
                    ncol = j+dc[k]

                    if nrow>=0 and nrow<n and ncol>=0 and ncol<n and grid[nrow][ncol]==1:
                        adjNode = nrow*n +ncol
                        compParent = ds.find(adjNode)
                        s.add(compParent)

                sizeSum=1
                for k in s:
                    sizeSum+=ds.size[k]
                
                ans=max(ans,sizeSum)
        
        for i in range(n*n):
            ans=max(ans,ds.size[i])
        return ans

grid = [[1, 1],
        [0, 1]]

ob=Solution()
print(ob.MaxConnection(grid))
