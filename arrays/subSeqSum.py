def subArrSum(arr, tar):
    n = len(arr)
    dp = {0: [[]]}  # Map of sum to list of subsequences

    for num in arr:
        # Update dp in reverse order to avoid overwriting results
        for s in list(dp.keys())[::-1]:
            new_sum = s + num
            if new_sum <= tar:
                if new_sum not in dp:
                    dp[new_sum] = []
                for subseq in dp[s]:
                    dp[new_sum].append(subseq + [num])

    return dp.get(tar, [])
