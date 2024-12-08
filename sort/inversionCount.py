class Solution:
    
    def merge(self,arr,low,high,mid):
        temp=[]
        l=low
        r=mid+1
        inv=0
        
        while l<=mid and r<=high:
            if arr[l]<=arr[r]:
                temp.append(arr[l])
                l+=1
            else:
                temp.append(arr[r])
                r+=1
                inv+=(mid-l+1)
        
        while l<=mid:
            temp.append(arr[l])
            l+=1
            
        while r<=high:
            temp.append(arr[r])
            r+=1
            
        for i in range(low,high+1):
            arr[i]=temp[i-low]
        
        return inv
            
            
    def mergeSort(self,arr, l, r):
        inv=0
        if l>=r: return inv
        mid=(l+r)//2
        
        inv+=self.mergeSort(arr,l,mid)
        inv+=self.mergeSort(arr,mid+1,r)
        inv+=self.merge(arr,l,r,mid)
        
        return inv
        
    def inversionCount(self, arr):
        n=len(arr)
        return self.mergeSort(arr,0,n-1)
        
