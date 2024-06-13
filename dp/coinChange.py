class Solution:
    def count(self, coins, N, Sum):
        dp=[[-1 for _ in range(Sum+1)] for _ in range(N+1)]

        def fun(coins,n,s):
            if s==0: return 1
            if n<1: return 0
            if s<0: return 0
            if dp[n][s]!=-1: return dp[n][s]
            dp[n][s]=fun(coins,n-1,s)+fun(coins,n,s-coins[n-1])
            return dp[n][s]
        return fun(coins,N,Sum)
    def count(self, coins, N, Sum):
        dp=[0]*(Sum+1)
        dp[0]=1
        for i in range(N):
            for j in range(1,Sum+1):
                if j>=coins[i]:
                    dp[j]=dp[j]+dp[j-coins[i]]
        return dp[Sum]
