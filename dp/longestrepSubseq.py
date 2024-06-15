class Solution:
	def LongestRepeatingSubsequence(self, str):
		n=len(str)
		s2=str
		dp=[[0 for _ in range(n+1)] for _ in range(n+1)]
		
		for i in range(1,n+1):
		    for j in range(1,n+1):
		        if i!=j and str[i-1]==s2[j-1]:
		          dp[i][j]=dp[i-1][j-1]+1
		        else:
		          dp[i][j]=max(dp[i-1][j],dp[i][j-1])
		return dp[n][n]
