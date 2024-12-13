class Solution:
    def findMin(self, arr):
        mi=float('inf')
        n=len(arr)
        l,r=0,n-1
        
        while l<=r:
            m=(l+r)//2
            if arr[l]<=arr[r]:
                return min(mi,arr[l])
        
            mi=min(arr[m],mi)
            
            if arr[m]>=arr[l]:
                l=m+1
            else:
                r=m-1
                
        return mi
