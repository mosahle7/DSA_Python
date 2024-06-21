from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        q=Queue()
        visited=[False]*(V)
        ans=[]
        q.put(0)
        visited[0]=True
        while not(q.empty()):
            cur=q.get()
            ans.append(cur)
            
            for i in adj[cur]:
                if visited[i]==False:
                    q.put(i)
                    visited[i]=True
        
        return ans
            
