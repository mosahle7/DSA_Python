class Solution:
    def lcmTriplets(self,n):
        if n==2 or n==1: return n
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        if n%2!=0: return n*(n-1)*(n-2)
        else:
            if gcd(n,n-3)==1:
                return n*(n-1)*(n-3)
            else:
                return (n-1)*(n-2)*(n-3)
