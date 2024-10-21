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
        
