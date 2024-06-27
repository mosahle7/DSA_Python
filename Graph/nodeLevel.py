from queue import Queue
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        l=0
        q=Queue()
        q.put((0,0))
        vis=[False]*V
        vis[0]=True
        while not(q.empty()):
            cur,ind=q.get()
            res.append(cur)
            l+=1
            for k in adj[cur]:
                if not(vis[k]):
                    if k==X: return ind+1
                    q.put((k,ind+1))
                    vis[k]=True
                    
        return -1
