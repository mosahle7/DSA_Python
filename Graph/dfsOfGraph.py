class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        vis=[False]*V
        ans=[]
        def dfs(s):
            vis[s]=True
            ans.append(s)
            for i in adj[s]:
                if not(vis[i]):
                    dfs(i)
        dfs(0)
        return ans
            
        
