
from typing import List
import math

class Solution:
    def MaxDiff(self, n : int, A : List[int]) -> int:
        m=-1
        maxArr=[float('-inf') for i in range(1000)]
        minArr=[float('inf') for i in range(1000)]
        for i in range(n):
            maxArr[A[i]-1]=max(maxArr[A[i]-1],i)
            minArr[A[i]-1]=min(minArr[A[i]-1],i)
        
        for i in range(1000):
            if maxArr[i]==float('-inf'):
                continue
            for j in range(i,1000):
                if maxArr[j]==float('-inf'):
                    continue
                if maxArr[i]==float('-inf'):
                    continue
            
                if math.gcd(i+1,j+1)!=1:
                    continue
                
                m=max(m,abs(maxArr[i]-minArr[j]))
                m=max(m,abs(minArr[i]-maxArr[j]))
      
        return m
