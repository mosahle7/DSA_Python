def subArrSum(arr,tar):
    n=len(arr)
    ans=[]
    l=0
    curSum=0
    for r in range(n):
        curSum+=arr[r]
        
        while l<=r and curSum>tar:
            curSum-=arr[l]
            l+=1
        
        if curSum==tar:
            ans.append(arr[l:r+1])
    return ans

def subArrSum(arr, tar):
    n = len(arr)
    ans = []
    cum_sum = 0
    sum_index = {0: -1}  # Cumulative sum to index map

    for i in range(n):
        cum_sum += arr[i]

        if cum_sum - tar in sum_index:
            start_index = sum_index[cum_sum - tar] + 1
            ans.append(arr[start_index:i + 1])

        sum_index[cum_sum] = i
    
    return ans

        
