class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0
        ans = 0
        for i in range(n - 1):
            x = max(x, nums[i])
            ans += x
        return ans

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n=len(nums)
        memo=[float('-inf') for _ in range(n)]
        def fun(i):
            if memo[i]!= float('-inf'): return memo[i]
            if i==n-1: return 0
            k=float('-inf')
            for j in range(i+1,n):
                k=max(k,((j-i)*nums[i])+fun(j))
            memo[i]=k
            return memo[i]
        return fun(0)

class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[n-1] = 0  # Base case: no score possible after the last element

        for i in range(n-2, -1, -1):  # Iterate backwards from the second-last element
            for j in range(i+1, n):
                dp[i] = max(dp[i], (j - i) * nums[i] + dp[j])
        
        return dp[0]

