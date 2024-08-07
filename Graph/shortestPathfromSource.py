
from typing import List

class Solution: 
    def shortestPath(self, V : int, m : int, edges : List[List[int]]) -> List[int]:
        dis=[float('inf')]*(V)
        dis[0]=0
        adj=[[] for _ in range(V)]
        for i in edges:
            adj[i[0]].append((i[1],i[2]))
    
        ind=[0]*(V)
        for i in adj:
            for j in i:
                ind[j[0]]+=1
                
        vis=[False]*(V)
        st=[]
        def dfs(i):
            vis[i]=True
            st.append(i)
            for j in adj[i]:
                ind[j[0]]-=1
                if not(vis[j[0]]) and ind[j[0]]==0:
                    dfs(j[0])
        
        for i in range(V):
            if ind[i]==0 and not(vis[i]):
                dfs(i)
                
        for i in st:
            if dis[i]!=float('inf'):
                for j in adj[i]:
                    if dis[j[0]]>(dis[i]+j[1]):
                        dis[j[0]]=dis[i]+j[1]
            
        
        for i in range(V):
            if dis[i]==float('inf'):
                dis[i]=-1
        
        return dis
                
