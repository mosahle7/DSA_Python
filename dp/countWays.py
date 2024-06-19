class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        mod=10**9+7
        if n==0 or n==1: return 1
        if n==2: return 2
        a,b,c=1,1,2
        
        for i in range(3,n+1):
            cur=(a+b+c)%mod
            a=b
            b=c
            c=cur
        return cur

#User function Template for python3

class Solution:
    #Function to count the number of ways in which frog can reach the top.
    def countWays(self,n):
        mod=10**9+7
        dp=[-1]*(n+1)
        arr=[1,2,3]
        def rec(n):
            if n==0: return 1
            if n<0: return 0
            if dp[n]!=-1: return dp[n]
            res=0
            for step in arr:
                res+=rec(n-step)%mod
            dp[n]=res
            return dp[n]%mod
        return rec(n)%mod
