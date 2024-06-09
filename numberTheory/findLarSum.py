class Solution:
    def findLargest(self, N, S):
        if N!=1 and S==0 : return -1
        if S>(9*N): return -1
        num=0
        for i in range(N-1,-1,-1):
            if S<9: 
                num+=(S*(10**i))
                S=0
            else:
                num+=(9*(10**i))
                S=S-9
        return num
    
class Solution:
    def findLargest(self, N, S):
        s=''
        if N!=1 and S==0 : return -1
        if S>(9*N): return -1

        for i in range(N):
            if S>=9:
                s=s+'9'
                S-=9

            else: 
                s=s+str(S)
                S=0
    
        return s

