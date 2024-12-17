import heapq
from collections import defaultdict

class Solution:
    def maxAmount(self, iniCurr: str, p1, r1, p2, r2):

        def build_graph(pair,rate):
            adj=defaultdict(list)
            for (u,v), r in zip(pair,rate):
                adj[u].append((v,r))
                adj[v].append((u,1/r))
            return adj

        def djikstra(start,adj,pr):
            h = [(-pr[node],node) for node in start]
            heapq.heapify(h)

            while h:
                curr,node = heapq.heappop(h)
                curr = -curr

                if curr<pr[node]:
                    continue
                    
                for neigh,rate in adj[node]:
                    upd = rate*curr
                    if upd>pr[neigh]:
                        pr[neigh] = upd
                        heapq.heappush(h,(-upd,neigh))
                
        pr = defaultdict(lambda: float('-inf'))
        pr[iniCurr] = 1.0  # Start with 1.0 of initial currency

        adj1 = build_graph(p1, r1)
        djikstra([iniCurr], adj1, pr)

        adj2 = build_graph(p2, r2)
        start_nodes = [node for node in pr if pr[node] > float('-inf')]  
        
        djikstra(start_nodes, adj2, pr)
        
        return pr[iniCurr]
