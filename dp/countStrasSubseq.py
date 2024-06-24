class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        n1,n2=len(s1),len(s2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        m=10**9+7
        
        for i in range(n1+1):
            dp[i][0]=1
        
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=(dp[i-1][j-1]%m+dp[i-1][j]%m)%m
                else:
                    dp[i][j]=dp[i-1][j]%m
        return dp[n1][n2]
