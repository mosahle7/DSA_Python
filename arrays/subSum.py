class Solution:
    def recSubSum(self, arr, n, sum):
        mod = 10**9 + 7
        memo = {}

        def fun(pos, current_sum):
            if current_sum < 0:
                return 0
            if pos == n:
                return 1 if current_sum == 0 else 0
            if (pos, current_sum) in memo:
                return memo[(pos, current_sum)]

            # Include the current element
            include = fun(pos + 1, current_sum - arr[pos]) % mod
            # Exclude the current element
            exclude = fun(pos + 1, current_sum) % mod

            # Store the result in the memo dictionary
            memo[(pos, current_sum)] = (include + exclude) % mod
            return memo[(pos, current_sum)]

        return fun(0, sum)

class Solution:
    def recMemSubSum(self, arr, n, sum):
        mod = 10**9 + 7
        dp=[[-1]*(sum+1) for i in range(n+1)]

        def fun(pos,sum):

            if sum<0: return 0
            if pos==n: return 1 if sum==0 else 0

            if dp[pos][sum]!=-1: return dp[pos][sum]

            dp[pos][sum] = (fun(pos+1,sum)%mod + fun(pos+1,sum-arr[pos])%mod)%mod

            return dp[pos][sum]
        
        return fun(0,sum)


class Solution:
    def dpSubSum(self, arr, n, sum):
        dp=[[0]*(sum+1) for i in range(n+1)]
        dp[0][0]=1

        for i in range(1,n+1):
            for j in range(sum+1):
                if j<arr[i-1]: dp[i][j]=dp[i-1][j]
                else: dp[i][j] = dp[i-1][j]+dp[i-1][j-arr[i-1]]
        
        return dp[n][sum]

class Solution:
    def dp1DSubSum(self, arr, n, sum):
        mod = 10**9 + 7

        dp = [0] * (sum + 1)
        dp[0] = 1

        for i in range(n):
            for j in range(sum, arr[i] - 1, -1):
                dp[j] = (dp[j] + dp[j - arr[i]]) % mod

        return dp[sum]%mod
