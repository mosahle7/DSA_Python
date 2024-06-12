from typing import List


class Solution:
    def trafficLights(self, n : int, q : int, queries : List[List[int]]) -> str:
        diff=[0]*(n+1)
        
        for i in range(q):
            start,end=queries[i]
            diff[start-1]+=1
            if end<n: diff[end]-=1
            
        cur=0
        arr=[]
        for i in range(n):
            cur+=diff[i]
            arr.append(cur)
        
        res=[]
        for k in arr:
            if k%3==1: res.append('Y')
            elif k%3==2: res.append('G')
            else: res.append('R')
        
        return (''.join(res))
            
