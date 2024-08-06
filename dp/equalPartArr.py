
class Solution:
    def equalPartition(self, N, arr):
        s=sum(arr)
        if s%2!=0: return 0
        
        half=s//2
        dp=[[-1 for _ in range(half+1)]for _ in range(N+1)]
        def fun(i,s):
            if s==half: return 1
            if s>half or i==N:
                return 0
            if dp[i][s]!=-1: return dp[i][s]
            
            dp[i][s]=(fun(i+1,s+arr[i]) or fun(i+1,s)) 
            return dp[i][s]
            
        return fun(0,0)

class Solution:
    def equalPartition(self, N, arr):
        s=sum(arr)
        if s%2!=0: return 0
        
        half=s//2
        dp=[False]*(half+1)
        
        dp[0]=1
        
        for num in arr:
            for s in range(half,num-1,-1):
                dp[s]=dp[s] or dp[s-num]
                
        return dp[half]
