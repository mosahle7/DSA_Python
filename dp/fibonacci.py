import sys
sys.setrecursionlimit(100000000)

class Solution:
    def topDown(self, n):
        mod = 10**9 + 7
        memo = [-1] * (n + 1)
        
        def fib(n):
            if n == 0 or n == 1: return n
            
            if memo[n] !=-1: return memo[n]
            memo[n] = (fib(n - 1) % mod + fib(n - 2) % mod) % mod
            return memo[n]
    
        return fib(n)
            
    def bottomUp(self, n):
        mod=10**9+7
        dp=[0]*(n+1)
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=(dp[i-1]%mod+dp[i-2]%mod)%mod
        return dp[n]
