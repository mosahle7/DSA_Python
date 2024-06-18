class Solution:
    def equalPartition(self, N, arr):
        S=sum(arr)
        if S%2!=0: return 0
        tar=S//2
        dp=[[-1 for _ in range(tar+1)] for _ in range(N+1)]
        def fun(s,ind):
            if dp[ind][s]!=-1: return dp[ind][s]
            if s==0: return 1
            if ind==N: return 0
            if s<0: return 0
            dp[ind][s]=fun(s-arr[ind],ind+1) | fun(s,ind+1)
            return dp[ind][s]
        return fun(tar,0)


class Solution:
    def equalPartition(self, N, arr):
        S = sum(arr)
        
        # If the total sum is odd, we cannot partition it into two equal subsets
        if S % 2 != 0:
            return 0
        
        tar = S // 2
        
        # DP array to store whether a sum is achievable
        dp = [False] * (tar + 1)
        dp[0] = True  # Zero sum is always achievable (with an empty subset)
        
        # Iterate over each element in the array
        for num in arr:
            # Update the DP array from back to front
            for j in range(tar, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return 1 if dp[tar] else 0
