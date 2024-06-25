from typing import List


class Solution:
    def minAmountRequired(self, n : int, sta : List[int], p : int) -> int:
        if p==1: return 1
        sta.append(10**9)
        sta.append(-10**9)
        sta.sort()
        
        l,r=1,p
        n+=2
        minCo=0
        
        while l<=r:
            mid=(l+r)//2
            needed=p
            cost=0
            remaining=mid
            picked=0
            
            for i in range(1,n-1):
                pickleft=remaining
                picked+=pickleft
                
                cost+=(pickleft*(pickleft+1))//2
                
                dist=sta[i+1]-sta[i]-1
                pickright=min(mid,(dist+1)//2)
                picked+=pickright
                
                cost+=(pickright*(pickright+1))//2
                remaining=min(mid,dist-pickright)
            
            if picked>=needed:
                minCo = cost-(mid*(picked-needed))
                r=mid-1
            else:
                l=mid+1
                
        return minCo
                
