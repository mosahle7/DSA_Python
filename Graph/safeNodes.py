from typing import List
from queue import Queue
class Solution:    
    def eventualSafeNodes(self, V : int, adj : List[List[int]]) -> List[int]:
        inDegree=[0]*V
        ans=[]
        revAdj=[[] for _ in range(V)]
        for i in range(V):
            for j in adj[i]:
                revAdj[j].append(i)
                inDegree[i]+=1
        
        q=Queue()
        for i in range(V):
            if inDegree[i]==0:
                q.put(i)
       
        while not(q.empty()):
            cur=q.get()
            ans.append(cur)
            for i in revAdj[cur]:
                inDegree[i]-=1
                if inDegree[i]==0:
                    q.put(i)
            
        ans.sort()
        return ans
