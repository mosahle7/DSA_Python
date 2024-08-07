class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        
        ans=1
        pl=1
        arr.sort()
        dep.sort()
        
        i=1
        j=0
        
        while i<n and j<n:
            if arr[i]<=dep[j]:
                pl+=1
                i+=1
            else:
                pl-=1
                j+=1
            
            if pl>ans:
                ans=pl
                
        return ans
    
