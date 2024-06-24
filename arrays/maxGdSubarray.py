from typing import List
class Solution:
    def maxGoodSubarrays(self, n: int, arr: List[int]) -> int:
        m=max(arr)
        if arr[-1]==m: return 0
        endpt=-1
        
        for i in range(n-2,-1,-1):
            if arr[i]>arr[n-1]:
                endpt=i
                break
        c=1
        ma=arr[0]
        for i in range(1,endpt):
            if arr[i]<ma:
                c+=1
                ma=arr[i+1]
            else:
                ma=arr[i]
        return c
