class Solution:
    def search(self,arr,key):
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==key:
                return mid
            
            if arr[l]<=arr[mid]:
                if arr[l]<=key<arr[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<key<=arr[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
