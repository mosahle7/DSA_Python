class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        
        indegree=[0]*V
        vis=[False]*V
        
        ans=[]
        for i in range(V):
            for j in adj[i]:
                indegree[j]+=1
        
        def dfs(i):
            vis[i]=True
            ans.append(i)
            for j in adj[i]:
                indegree[j]-=1
                if indegree[j]==0 and not(vis[j]):
                    dfs(j)
        
        for i in range(V):
            if indegree[i]==0 and not(vis[i]):
                dfs(i)
        return ans
            
