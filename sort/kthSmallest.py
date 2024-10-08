class Solution:
    def kthSmallest(self, arr, l, r, k):
        def partition(arr,l,r):
            i=l-1
            piv=arr[r]
            for j in range(l,r):
                if arr[j]<piv:
                    i+=1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[r]=arr[r],arr[i+1]
            return i+1
        def quickSel(arr,l,r,k):
            if l<=r:
                pivInd=partition(arr,l,r)
                if pivInd==k: return arr[pivInd]
                elif pivInd>k: return quickSel(arr,l,pivInd-1,k)
                else: return quickSel(arr,pivInd+1,r,k)
            
        return quickSel(arr,l,r,k-1)
            

class Solution:

    def kthSmallest(self, arr,k):
        n=len(arr)
        ma=max(arr)
        ch=[0]*(ma+1)
        
        for i in range(n):
            ch[arr[i]]=1
        
        for i in range(ma+1):
            if ch[i]==1:
                k-=1
            if k==0: 
                return i
            
