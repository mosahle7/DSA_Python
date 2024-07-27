class Solution:
    def countMin(self, str):
        if str==str[::-1]:
            return 0
        n=len(str)
        def lcs(S):
            S2=S[::-1]
            
            dp=[[0]*(n+1) for _ in range(n+1)]
            
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if S[i-1]==S2[j-1]:
                        dp[i][j]=dp[i-1][j-1]+1
                    else:
                        dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
            return dp[n][n]
            
        l=lcs(str)
        return n-l
