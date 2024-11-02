from typing import List
import heapq

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj=[[] for i in range(n)]
        dis=[float('inf')]*n
        dis[src]=0
        
        for fl in flights:
            f,t,p=fl
            adj[f].append((t,p))
        
        h=[(0,src,0)]
        
        while h:
            stops,city,p1=heapq.heappop(h)
        
            for fl in adj[city]:
                new,p2=fl
                if new == dst and p1+p2<dis[new]:
                    dis[new]=p1+p2
                    
                elif stops+1<=k:
                    if p1+p2<dis[new]:
                        dis[new]=p1+p2
                        heapq.heappush(h,(stops+1,new,dis[new]))
                        
        return dis[dst] if dis[dst]!=float('inf') else -1


from queue import deque
from typing import List

class Solution:
    def CheapestFLight(self,n,flights,src,dst,k):
        adj=[[] for i in range(n)]
        dis=[float('inf')]*n
        dis[src]=0
        
        for fl in flights:
            f,t,p=fl
            adj[f].append((t,p))
        
        h=deque([(0,src,0)])
        
        while h:
            stops,city,p1=h.popleft()
        
            for fl in adj[city]:
                new,p2=fl
                if new == dst and p1+p2<dis[new]:
                    dis[new]=p1+p2
                    
                elif stops+1<=k:
                    if p1+p2<dis[new]:
                        dis[new]=p1+p2
                        h.append((stops+1,new,dis[new]))
                        
        return dis[dst] if dis[dst]!=float('inf') else -1
                
            
