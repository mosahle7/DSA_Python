class Solution:
	def nthRowOfPascalTriangle(self,n):
		mod=10**9+7
		a1=[1]
		a2=[1,1]
		if n == 1: return a1 
		if n == 2: return a2
		
	    for i in range(3,n+1):
            if i%2==0:
                a2=[1]*i
				for j in range(i):
				    if not(j==0 or j==i-1):
					    a2[j]=(a1[j-1]+a1[j])%mod
					
            else:
                a1=[1]*i
				for j in range(i):
					if not(j==0 or j==i-1):
						a1[j]=(a2[j-1]+a2[j])%mod
    
        if n%2==0: return a2
		else: return a1
