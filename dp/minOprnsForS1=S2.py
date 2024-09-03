class Solution:
	def minOperations(self, str1, str2):
	    n1,n2=len(str1),len(str2)
	    
		dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]
		
		for i in range(n1+1):
		    dp[i][0]=i
		
		for j in range(n2+1):
		    dp[0][j]=j
		   
		
		for i in range(1,n1+1):
		    for j in range(1,n2+1):
		        if str1[i-1]==str2[j-1]:
		            dp[i][j]=dp[i-1][j-1]
		        else:
		            dp[i][j]=min(dp[i-1][j],dp[i][j-1])+1
		return dp[n1][n2]
