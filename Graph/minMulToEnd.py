from typing import List
from queue import Queue
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mi=0
        
        if (end%start)!=0:
            return -1
        
        while start!=end:
            ma=float('-inf')
            for i in range(n):
                k=start*arr[i]
                if end%k==0:
                    ma=max(ma,k)
            
            if ma!=float('-inf'):
                start=ma
                mi+=1
            else: return -1
                
        
        return mi

class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        mod=10**5
        q=Queue()
        pro=set()
        q.put(start%mod)
        level=0
        
        while not(q.empty()):
            size=q.qsize()
            for i in range(size):
                t=q.get()
                if t==end: return level
                
                for j in range(n):
                    toAdd=(t%mod*arr[j]%mod)%mod
                    if toAdd not in pro:
                        q.put(toAdd)
                        pro.add(toAdd)
            
            level+=1
        
        return -1
                    
