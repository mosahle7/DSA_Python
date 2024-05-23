from typing import List
class Solution:
    def maxAlternatingSubstring(self, n : int, s : str) -> int:
   
        i=0
        lens=[]
        while i<n:
            j=i+1
            while j<n and s[j]!=s[j-1]:
                j+=1
            lens.append(j-i)
            i=j
    
        lens.append(0)

        ansBefore = 0
        for i in lens:
            ansBefore+=(i*(i+1))//2
    
        ans=0

        for i in range(len(lens)-1):
            a=lens[i]
            b=lens[i+1]
            curAns= ansBefore - ((a*(a+1))/2) - ((b*(b+1))/2) + (((a+b+1)*(a+b+2))/2)
            ans = max(ans,curAns)

        return int(ans)
        
