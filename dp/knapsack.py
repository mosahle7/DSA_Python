#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        n=len(wt)
        dp=[[-1]*(W+1) for _ in range(n+1)]
        def fun(i,w):
            if i==n: return 0
            if w<=0: return 0
            if dp[i][w]!=-1: return dp[i][w]
            
            take=0
            if wt[i]<=w:
                take=val[i]+fun(i+1,w-wt[i])
                
            noTake=fun(i+1,w)
            dp[i][w]=max(take,noTake)
            return dp[i][w]
            
        return fun(0,W)
            
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        n=len(wt)
        dp=[[0]*(W+1) for _ in range(n+1)]
        
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1]<=j:
                    dp[i][j]=max(dp[i-1][j],val[i-1]+dp[i-1][j-wt[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][W]


class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
        n=len(wt)
        # dp=[[0]*(W+1) for _ in range(n+1)]
        dp=[0]*(W+1)
        for i in range(1,n+1):
            for j in range(W,wt[i-1]-1,-1):
                if wt[i-1]<=j:
                    dp[j]=max(dp[j],val[i-1]+dp[j-wt[i-1]])
                else:
                    dp[j]=dp[j]
        return dp[W]
