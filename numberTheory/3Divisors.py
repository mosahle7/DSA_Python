#User function Template for python3

import math
class Solution:
    def threeDivisors(self, query, q):
        ans=[]
        primes=[1]*(10**6)
        primes[0]=0
        for j in range(2,10**3+1):
                if primes[j-1]==1:
                    for m in range(j*j,10**6+1,j):
                        primes[m-1]=0
    
        for p in range(2,10**6+1):
            primes[p-1]+=primes[p-2]
            
                        
        
        for i in range(q):
            qr=int(math.sqrt(query[i]))
            c=primes[qr-1]
            ans.append(c)
            
        return ans
        
import math
class Solution:
    def threeDivisors(self, query, q):
        ans=[]
        
        for i in range(q):
            qr=int(math.sqrt(query[i]))
            primes=[True]*(qr)
            primes[0]=False
        
            for j in range(2,int(math.sqrt(qr))+1):
                if primes[j-1]:
                    for m in range(j*j,qr+1,j):
                        primes[m-1]=False
                        
            c=0
            for p in primes:
               if primes[p]: c+=1
            ans.append(c)
            
        return ans
