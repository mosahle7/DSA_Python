
class Solution:
    def findOnce(self,arr : list, n : int):
        if n==1:
            return arr[0]
        # Complete this function
        l,r=0,n-1
        
        while l<=r:
            mid=(l+r)//2
            
            if mid%2==1:
                if mid-1>=0 and arr[mid]==arr[mid-1]:
                    l=mid+1
                elif mid+1<n and arr[mid]==arr[mid+1]:
                    r=mid-1
                else:
                    return arr[mid]
            
            else:
                if mid+1<n and arr[mid]==arr[mid+1]:
                    l=mid+2
                elif mid-1>=0 and arr[mid]==arr[mid-1]:
                    r=mid-2
                else:
                    return arr[mid]
            
