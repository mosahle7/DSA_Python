class Solution:
    def findMaxProduct(self, arr):
        mod=10**9+7
        n=len(arr)
        if n==1:
            return arr[0]
        for i in range(n):
            if arr[i]!=0:
                break
            if i==n-1:
                return 0
                
        pro=1
        nN=0
        nZ=0
        nP=0
        maxN=float('-inf')
        for i in range(n):
            if arr[i]>0:
                pro*=arr[i]
                nP+=1
            elif arr[i]<0:
                pro*=arr[i]
                nN+=1
                maxN=max(maxN,arr[i])
            else:
                nZ+=1
        
        if n==2 and nN%2!=0 and nZ>0 and nP==0:
            return 0
        elif nN%2!=0:
            pro=(pro//maxN)
        
        return pro%mod
