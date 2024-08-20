class Solution:
    def getSmallest(self, N):
        if N<10: return N
        
        s=''
        for i in range(9,1,-1):
            while N>1 and N%i==0:
                s=str(i)+s
                N//=i
            
        if N!=1:
            return -1
        
        return s

class Solution:
    def getSmallest(self, N):
        if N<10: return N
        
        dig=[]
        for i in range(9,1,-1):
            while N>1 and N%i==0:
                dig.append(i)
                N//=i
            
        if N!=1:
            return -1
        
        res=0
        l=len(dig)
        
        while l!=0:
            res=res*10+dig[-1]
            dig.pop()
            l-=1
        
        return res
