class Solution:
    def printAllDups(self, root):
        d={}
        ans=[]
        def dfs(root):
            if root is None: return '#'
            
            cur=str(root.data)
            
            cur+=dfs(root.left)
            cur+=dfs(root.right)
            
            if cur in d:
                d[cur]+=1
                if d[cur]==2:
                    ans.append(root)
            else:
                d[cur]=1
        
            return cur
        
        dfs(root)
        
        return ans
