class Solution:
    def perfectSum(self, arr, n, sum):
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
