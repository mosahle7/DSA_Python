
class Solution:
    def padovanSequence(self, n):
        mod=10**9+7
        a,b,c=1,1,1
        if n==0 or n==1 or n==2: return 1
        
        for i in range(3,n+1):
            d=((a%mod)+(b%mod))%mod
            a=b
            b=c
            c=d
        return d
