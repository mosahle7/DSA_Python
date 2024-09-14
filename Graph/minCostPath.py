
import heapq

class Solution:
    def minimumCostPath(self, grid):
        n=len(grid)
        li=[[float('inf')]*n for _ in range(n)]
        li[0][0]=grid[0][0]
        # vis=set()
        # vis.add((0,0))
        
        h=[[grid[0][0],(0,0)]]
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n
            
        while len(h)!=0:
            dis,ind=heapq.heappop(h)
            # vis.add(ind)
            if ind==(n-1,n-1):
                return d
            for k in range(4):
                x=ind[0]+dx[k]
                y=ind[1]+dy[k]
                
                if isSafe(x,y):
                    if dis+grid[x][y]<li[x][y]:
                        li[x][y]=dis+grid[x][y]
                        heapq.heappush(h,[li[x][y],(x,y)])
                    

from sortedcontainers import SortedSet
class Solution:
    def minimumCostPath(self, grid):
        n=len(grid)
        li=[[float('inf')]*n for _ in range(n)]
        li[0][0]=grid[0][0]
        
        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        s=SortedSet()
        s.add((grid[0][0],(0,0)))
        
        while len(s)!=0:
            dis,ind=s.pop(0)
            if ind==(n-1,n-1):
                return dis
            for k in range(4):
                x=ind[0]+dx[k]
                y=ind[1]+dy[k]
                
                if isSafe(x,y):
                    if dis+grid[x][y]<li[x][y]:
                        if li[x][y]!=float('inf'):
                            s.remove((li[x][y],(x,y)))
                        li[x][y]=dis+grid[x][y]
                        s.add((li[x][y],(x,y)))
