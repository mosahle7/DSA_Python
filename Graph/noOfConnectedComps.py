class Solution:
    def numProvinces(self, adj, V):
        vis=[False]*V
        # ans=[]
        c=0
        def dfs(s):
            vis[s]=True
            # ans.append(s)
            for i in range(V):
                if s!=i and adj[s][i]==1 and not(vis[i]):
                    dfs(i)
                    
        for i in range(V):
            if not(vis[i]):
                c+=1
                dfs(i)
        return c
            
