class Solution:
    def isSumOfTwo (self, N):
        def prime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                  return False
            return True
        if N<=3: return "No"
        elif N%2==0: return "Yes"
        
        else:
            if prime(N-2): return "Yes"
        
        return "No"


class Solution:
    def isSumOfTwo (self, N):
        def prime(n):
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                   return False
            return True
        for i in range(2,N//2+1):
            if prime(i) and prime(N-i):
                    return "Yes"
                    
        return 'No'


#User function Template for python3
class Solution:
    def isSumOfTwo (self, N):
        primes=[True]*(N+1)
        primes[0],primes[1]=False,False
        
        for i in range(2,int(N**0.5)+1):
            if primes[i]:
                j=i*i
                while j<=N:
                    primes[j]=False
                    j+=i
        
        for i in range(2,N+1):
            if primes[i]:
                if primes[N-i]:
                    return "Yes"
                    
        return 'No'
