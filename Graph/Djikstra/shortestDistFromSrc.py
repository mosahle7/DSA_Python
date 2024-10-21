import heapq

class Solution:
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        n=len(adj)
        dis=[float('inf') for _ in range(n)]
        
        h=[[0,src]]
        dis[src]=0
        heapq.heapify(h)
        
        while h:
            dist,node=heapq.heappop(h)
            for k in adj[node]:
                if dis[k[0]]>k[1]+dist:
                    heapq.heappush(h,[k[1]+dist,k[0]])
                    dis[k[0]]=k[1]+dist
        return dis

from sortedcontainers import SortedSet

class Solution:
    def dijkstra(self, adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
        n=len(adj)
        dis=[float('inf') for _ in range(n)]
        s=SortedSet()
        
        s.add((0,src))
        dis[src]=0

        while s:
            dist,node=s.pop(0)
            for k in adj[node]:
                
                if dis[k[0]]>k[1]+dist:
                    if dis[k[0]]!=float('inf'):
                        s.remove((dis[k[0]],k[0]))
                        
                    s.add((k[1]+dist,k[0]))
                    dis[k[0]]=k[1]+dist
        return dis
        
