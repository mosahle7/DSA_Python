def robo(mat):
    m=len(mat)
    n=len(mat[0])
    
    dx=[1,0]
    dy=[0,1]
    
    memo=[[None]*n for _ in range(m)]
    
    def isSafe(x,y):
        return x<m and y<n
    
    def fun(i,j):
        
        if i==m-1 and j==n-1:
            return 1
        
        if memo[i][j] is not None:
            return memo[i][j]
        
        min_health=float('inf')
        
        for k in range(2):
            x=i+dx[k]
            y=j+dy[k]
            if isSafe(x,y):
                min_health=min(min_health,fun(x,y))
        
        memo[i][j] = max(1,min_health-mat[i][j])
        return memo[i][j]
        
    return fun(0,0)

mat=[[0, -3,2],[-1 ,-5, 0]]
print(robo(mat))
