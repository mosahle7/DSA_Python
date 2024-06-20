class Solution:
	def totalWays(self, n, cap):
	    mod=10**9+7
		cap.sort()
		ans=cap[0]
		for i in range(1,n):
		    ans=(ans*(cap[i]-i))%mod
		
		return ans
