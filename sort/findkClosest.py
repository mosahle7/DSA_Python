class Solution:
    def printKClosest(self, arr, n, k, x):
        ind=helper(arr,0,n-1,x)
        res=[]
        def helper(arr,low,high,x):
            if arr[low]>=x:
                return low
            if arr[high]<=x:
                return high
            
            m=(low+high)/2

            if arr[m]<=x and arr[m+1]>x:
                return m

            elif arr[m]<x:
                return helper(arr,m+1,high,x) 
            else:
                return helper(arr,low,m-1,x) 
        
        r=ind+1
        if arr[ind]==x:
            l=ind-1
        else:
            l=ind

        while k and l>=0 and r<n:
            if x-arr[l]<arr[r]-x:
                res.append(arr[l])
                l-=1
            else:
                res.append(arr[r])
                r+=1
            k-=1

        while k and l>=0:
            res.append(arr[l])
            l-=1
            k-=1

        while k and r<n:
            res.append(arr[r])
            r+=1
            k-=1
        return res
        
        






