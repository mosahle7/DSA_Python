from typing import List
import heapq
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        h=[(0,start)]
        vis=set([start])
        m=10**5
        while h:
            moves,st=heapq.heappop(h)
            if st==end:
                return moves
            for k in arr:
                if (st*k)%m not in vis:
                    heapq.heappush(h,(moves+1,(st*k)%m))
                    vis.add((st*k)%m)
        return -1
    
