class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        if n==0: return 0
        dp=[1]*(n)
        for i in range(1,n):
            for j in range(i):
                if a[i]>a[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
       

