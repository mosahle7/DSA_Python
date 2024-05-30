
class Solution:
    def perfectSum(self, arr, n, sum):
        mod = 10**9 + 7

        dp = [0] * (sum + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(sum, arr[i] - 1, -1):
                dp[j] = (dp[j] + dp[j - arr[i]]) % mod

        return dp[sum]%mod


class Solution:
	def findMinCost(self, x, y, costX, costY):
		n,m = len(x),len(y)
		dp=[[0]*(m+1) for i in range(n+1)]
		
		for i in range(1,n+1):
			for j in range(1,m+1):
				if x[i-1]==y[j-1]:
					dp[i][j]=dp[i-1][j-1]+1
				else: 
					dp[i][j]=max(dp[i-1][j],dp[i][j-1])
		leng=dp[n][m]
		tcost = (n-leng)*costX + (m-leng)*costY
		return tcost
            
