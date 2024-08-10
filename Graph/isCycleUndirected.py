from typing import List
from collections import deque
class Solution:
    Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    vis=[False]*V
		def dfs(i,par):
		    vis[i]=True
		    for k in adj[i]:
		        if not(vis[k]):
		            if dfs(k,i)==True:
		                return True
		               
		        elif k!=par:
		            return True
		            
		    return False
		    
		for i in range(V):
		    if not(vis[i]):
		        if dfs(i,-1): return 1
		return 0
		        
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    vis=[False]*V
	    q=deque()
	    for i in range(V):
	        if not(vis[i]):
	            q.append((i,-1))
	        while len(q)!=0:
	            node,par=q.popleft()
	            vis[node]=True
	            for k in adj[node]:
	                if not(vis[k]):
	                    q.append((k,node))
	                elif k!=par:
	                    return 1
	    return 0
	               
