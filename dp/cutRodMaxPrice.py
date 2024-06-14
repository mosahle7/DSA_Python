
class Solution:
    def cutRod(self, price, n):
        dp=[0]*(n+1)
        dp[0]=0
        
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j>=i:
                    dp[j]=max(dp[j],(dp[j-i]+price[i-1]))
        return dp[n]
