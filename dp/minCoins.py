class Solution:
	def minCoins(self, coins, M, sum):
		memo={}
		def fun(s):
		    if s==sum: return 0
		    if s>sum: return float('inf') 
		    if s in memo: return memo[s]
		    
		    minCoins=float('inf')
		    
		    for i in range(m):
		        res=fun(s+coins[i])
		        if res!=float('inf'):
		            minCoins=min(minCoins,res+1)
		    memo[s]=minCoins
		    return memo[s]
		res=fun(0)
		return res if res!=float('inf') else -1
		
		def minCoins(self, coins, M, sum):
		    dp=[float('inf')]*(sum+1)
		    dp[0]=0
		    for i in range(M):
		        for j in range(1,sum+1):
		            if j>=coins[i]:
		                dp[j]=min(dp[j],dp[j-coins[i]]+1)
		    return dp[sum] if dp[sum]!=float('inf') else -1
		    
	def minCoins(self, coins, M, sum):
        memo={}
		def fun(i,s):
		    if s>sum or i==M: return float('inf')
		    if s==sum: return 0
		    if s in memo: return memo[(i,s)]
		        
            minC=float('inf')
		    inc=fun(i,s+coins[i])
		    exc=fun(i+1,s)
		        
		    minC=min(minC,inc+1,exc)
		    memo[(i,s)]=minC
		    return memo[(i,s)]
        ans=fun(0,0)
		return ans if ans!=float('inf') else -1
