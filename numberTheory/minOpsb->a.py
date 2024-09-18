import math
class Solution:
    def minOps(self, a : int, b : int) -> int:
        if b<a: return -1
        op=0
        st=True
        while b!=a:
            s=int(math.sqrt(b))
            if s**2>b:
                s-=1
            
            if s**2==b and st:
                if s>=a:
                    b=s
                    op+=1
                else:
                    st=False
                    op+=(b-a)
                    b=a
            elif s**2!=b and st:
                op+=(b-(s**2))
                b=s**2
            else:
                op+=(b-a)
                b=a
                
        return op
