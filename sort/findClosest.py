from typing import List
class Solution:
    def findClosest(self, n : int, k : int, arr : List[int]) -> int:
        l,h=0,n-1
        ans=arr[0]

        while l<=h:
            mid = (l+h)//2
            if abs(ans-k)==abs(arr[mid]-k):
                ans= max(ans,arr[mid])
            elif abs(ans-k)>abs(arr[mid]-k):
                ans = arr[mid]
            
            if arr[mid] == k:
                return arr [mid]
            elif arr[mid]<k:
                l=mid+1
            else:
                h=mid-1
        return ans
