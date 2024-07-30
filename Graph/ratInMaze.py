from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        if m[0][0]==0:
            return []
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        le=['U','R','D','L']
        ans=[]
        
        vis=set()
        vis.add((0,0))
        def isSafe(x,y):
            if 0<=x<n and 0<=y<n and m[x][y]==1:
                return True
            return False
            
        def dfs(x,y,s):
            
            if x==n-1 and y==n-1:
                ans.append(s)
                return
                
            for i in range(4):
                xc=x+dx[i]
                yc=y+dy[i]
                if isSafe(xc,yc) and (xc,yc) not in vis:
                    vis.add((xc,yc))
                    dfs(xc,yc,s+le[i])
                    vis.remove((xc,yc))
            
            return
                    
        dfs(0,0,'')
                    
        return ans
                
