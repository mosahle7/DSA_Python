
class Solution:
    def perfectSum(self, arr, n, sum):
        mod = 10**9 + 7

        dp = [0] * (sum + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(sum, arr[i] - 1, -1):
                dp[j] = (dp[j] + dp[j - arr[i]]) % mod

        return dp[sum]%mod
            
