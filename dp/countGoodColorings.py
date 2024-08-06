def count_good_colorings(arr, k):
    n = len(arr)
    total_sum = sum(arr)
    
    # Initialize the DP table
    dp = [[[0 for _ in range(k)] for _ in range(k)] for _ in range(n+1)]
    dp[0][0][0] = 1  # Base case
    
    # Iterate through each element in the array
    for i in range(n):
        for r in range(k):
            for g in range(k):
                if dp[i][r][g] > 0:
                    # Calculate new states
                    red_r = (r + arr[i]) % k
                    green_g = (g + arr[i]) % k
                    dp[i+1][red_r][g] += dp[i][r][g]
                    dp[i+1][r][green_g] += dp[i][r][g]
                    dp[i+1][r][g] += dp[i][r][g]

    # Count valid colorings
    count = 0
    
    # Check each state in the final DP table
    for r in range(k):
        for g in range(k):
            b = (total_sum - r - g) % k
            if (r + g) % k == b % k or r % k == (g + b) % k:
                count += dp[n][r][g]
    
    return dp

# Example usage:
arr = [2,4]
k = 2
print(count_good_colorings(arr, k))  

def count_good_colorings(arr, k):
    n = len(arr)
    total_sum = sum(arr)
    
    # Initialize the DP table
    dp_prev = [[0 for _ in range(k)] for _ in range(k)]
    dp_prev[0][0] = 1  # Base case

    # Iterate through each element in the array
    for i in range(n):
        dp_curr = [[0 for _ in range(k)] for _ in range(k)]
        for r in range(k):
            for g in range(k):
                if dp_prev[r][g] > 0:
                    # Calculate new states
                    red_r = (r + arr[i]) % k
                    green_g = (g + arr[i]) % k
                    dp_curr[red_r][g] += dp_prev[r][g]
                    dp_curr[r][green_g] += dp_prev[r][g]
                    dp_curr[r][g] += dp_prev[r][g]
        dp_prev = dp_curr

    # Count valid colorings
    count = 0
    
    # Check each state in the final DP table
    for r in range(k):
        for g in range(k):
            b = (total_sum - r - g) % k
            if (r + g) % k == b % k or r % k == (g + b) % k:
                count += dp_prev[r][g]
    
    return dp_prev

def rgb(arr,n,k):
    t=sum(arr)

    def fun(i,r,g):
        if i==n:
            if ((r+g)%k == (t-(r+g))%k) or (r%k == (g+ (t-(r+g)))%k):
                return 1
            return 0
            
        return fun(i+1,r+arr[i],g)+fun(i+1,r,g+arr[i])+fun(i+1,r,g)
    return fun(0,0,0)

