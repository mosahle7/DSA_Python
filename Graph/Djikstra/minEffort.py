from collections import deque
import heapq
from typing import List


class Solution:
    def MinimumEffort(self, n : int, m : int, hs : List[List[int]]) -> int:
        h=[(0,(0,0))]
      
        dis=[[float('inf') for _ in range(m)]for _ in range(n)]
        
        dis[0][0]=0
        dx=[0,-1,0,1]
        dy=[-1,0,1,0]
        
        def isSafe(x,y):
            return 0<=x<n and 0<=y<m
            
        while h:
            dist,node=heapq.heappop(h)
            if node==(n-1,m-1):return dis[n-1][m-1]
            nx,ny=node
        
            for k in range(4):
                x=nx+dx[k]
                y=ny+dy[k]
                if isSafe(x,y):
                    if max(dist,abs(hs[nx][ny]-hs[x][y]))<dis[x][y]:
                        heapq.heappush(h,(max(dis[nx][ny],abs(hs[nx][ny]-hs[x][y])),(x,y)))
                        dis[x][y]=max(dist,abs(hs[nx][ny]-hs[x][y]))
