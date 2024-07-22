class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        n=len(arr)
        maxSoFar=arr[0]
        maxEnd=arr[0]
        for i in range(1,n):
            maxEnd=max(maxEnd+arr[i],arr[i])
            maxSoFar=max(maxSoFar,maxEnd)
        
        return maxSoFar
