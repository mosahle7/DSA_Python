class Solution:

    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n=len(stalls)
        
        l,r=1,stalls[-1]-stalls[0]
        
        def feasibility(mid):
            num=1
            last=stalls[0]
            
            for i in range(1,n):
                if stalls[i]-last>=mid:
                    last=stalls[i]
                    num+=1
                if num==k:
                    return True
            return False
            
        res=0  
        while l<=r:
            mid=(l+r)//2
    
            if feasibility(mid):
                res=mid
                l=mid+1
             
            else:
                r=mid-1
            
        return res
