class Solution:
	def maxSumIS(self, arr, n):
	    dp=arr[:]
	    for i in range(1,n):
	        for j in range(i):
	            if arr[i]>arr[j]:
	                dp[i]=max(dp[i],dp[j]+arr[i])
	    return max(dp)
