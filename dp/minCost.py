class Solution:
    def minimizeCost(self, k, arr):
        memo={}
        n=len(arr)
        
        def fun(i):
            if i==n-1: return 0
        
            if i in memo:return memo[i]
            
            p=float('inf')
            for m in range(1,k+1):
                if i+m<n:
                    cost=fun(i+m)+abs(arr[i]-arr[i+m])
                    p=min(p,cost)
                    
            memo[i]=p
            return memo[i]
        return fun(0)
