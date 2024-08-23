class Solution:
    def nextPermutation(self, N, arr):
        ind=-1
        for i in range(N-2,-1,-1):
            if arr[i]<arr[i+1]:
                ind=i
                break
        if ind==-1: return arr[::-1]
        
        
        for j in range(N-1,ind,-1):
            if arr[j]>arr[ind]:
                arr[ind],arr[j]=arr[j],arr[ind]
                break
            
        arr[ind+1:]=arr[ind+1:][::-1]
        return arr
                    
