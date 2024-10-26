from collections import deque
from typing import List

class Solution:
    
    def shortestPath(self, grid: List[List[int]], src: List[int], dest: List[int]) -> int:
        h=deque([(0,src)])
        n=len(grid)
        m=len(grid[0])
        dis=[[float('inf') for _ in range(m)]for _ in range(n)]
        
        if grid[src[0]][src[1]]==0 or grid[dest[0]][dest[1]]==0: return -1
        if src==dest: return 0
        
        dis[src[0]][src[1]]=0
        dx=[0,-1,0,1]
        dy=[-1,0,1,0]
        
        def isSafe(x,y):
            return 0<=x<n and 0<=y<m and grid[x][y]==1
            
        while h:
            dist,node=h.popleft()
            for k in range(4):
                x=node[0]+dx[k]
                y=node[1]+dy[k]
                if isSafe(x,y):
                    if dist+1<dis[x][y]:
                        h.append((dist+1,[x,y]))
                        dis[x][y]=dist+1
                    if [x,y]==dest: return dis[x][y]
        
        return -1
