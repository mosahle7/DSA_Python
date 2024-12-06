class Solution:
    # Function to find hIndex
    def hIndex(self, cits):
        ans=0
        n=len(cits)
        d={}
        cits.sort()
        for i in range(n):
            if cits[i] not in d:
                d[cits[i]]=1
            else:
                d[cits[i]]+=1
        co=0
        
        for i in range(n+1):
            if i in d:
                co+=d[i]
                t=d[i]+n-co
            else:
                t=n-co
            if t>=i:
                ans=i
        return ans
            

class Solution:
    # Function to find hIndex
    def hIndex(self, cits):
        h=0
        n=len(cits)
        
        cits.sort(reverse=True)
        
        for i in range(n):
            if cits[i]>=i+1:
                h=i+1
            else:
                break
        return h
