import heapq
from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        h=[(0,1)]
        par=[(i+1) for i in range(n)]
        
        dis=[float('inf') for _ in range(n)]
        dis[0]=0
        
        adj=[[] for _ in range(n)]
        for k in edges:
            adj[k[0]-1].append((k[1],k[2]))
            adj[k[1]-1].append((k[0],k[2]))
        
        while h:
            dist,node=heapq.heappop(h)
            for neigh in adj[node-1]:
                if dist+neigh[1]<dis[neigh[0]-1]:
                    dis[neigh[0]-1]=dist+neigh[1]
                    par[neigh[0]-1]=node
                    heapq.heappush(h,(dist+neigh[1],neigh[0]))
        
        if dis[n-1]==float('inf'): return [-1]
        ans=[]
        
        i=n-1
        while par[i]!=i+1:
            ans.append(i+1)
            i=par[i]-1
        ans.append(1)
        ans.append(dis[n-1])
        
        return ans[::-1]
