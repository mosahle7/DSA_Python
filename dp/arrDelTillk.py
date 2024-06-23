def arrDelTillk(n,k):  
    arr= tuple(range(n))
    ele=k-1
    memo={}
    def fun(arr):
        if arr in memo: return memo[arr]
        if len(arr)==1:
            if arr[0]==ele: return 1
            else: return 0
        res=fun(arr[1:])+fun(arr[:-1])
        memo[arr]=res
        return memo[arr]

    return fun(arr)
def arrDelTillk(n, k):
    arr = tuple(range(n))
    ele = k - 1
    dp = [[0] * n for _ in range(n)]
    
    # Base cases
    for i in range(n):
        if arr[i] == ele:
            dp[i][i] = 1
        else:
            dp[i][i] = 0
    
    # Fill DP table
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = dp[i + 1][j] + dp[i][j - 1]
    
    # The result is the number of ways to reduce the whole array [0...n-1] to ele
    return dp[0][n - 1]
