class Solution:
    def fill(self, n, m, mat):
        def valid(i,j):
            if 0<=i<n and 0<=j<m:
                return True
            return False
        
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        
        def dfs(i,j):
            if not(valid(i,j)):
                return 
            
            if mat[i][j]=='O':
                mat[i][j]='-'
                for k in range(4):
                    dfs(i+dr[k],j+dc[k])
        
        for j in range(m):
            if mat[0][j]=='O':
                mat[0][j]='-'
                for k in range(4):
                    dfs(0+dr[k],j+dc[k])
            if mat[n-1][j]=='O':
                mat[n-1][j]='-'
                for k in range(4):
                    dfs(n-1+dr[k],j+dc[k])
        
        for i in range(n):
            if mat[i][0]=='O':
                mat[i][0]='-'
                for k in range(4):
                    dfs(i+dr[k],0+dc[k])
            if mat[i][m-1]=='O':
                mat[i][m-1]='-'
                for k in range(4):
                    dfs(i+dr[k],m-1+dc[k])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]=='-':
                    mat[i][j]='O'
                elif mat[i][j]=='O':
                    mat[i][j]='X'
                    
        return mat
