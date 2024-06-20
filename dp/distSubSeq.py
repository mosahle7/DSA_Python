#User function Template for python3

class Solution:
    def distinctSubsequences(self, S):
        n=len(S)
        dp=[0]*(n+1)
        m=10**9+7
        dp[0]=1
        d={}
        for i in range(1,n+1):
            dp[i]=(2*dp[i-1])%m
            
            if S[i-1] in d:
                dp[i]=(dp[i]-dp[d[S[i-1]]-1])%m
            
            d[S[i-1]]=i
        return dp[n]
