class Solution:
    def largestPrimeFactor (self, N):
        d=[True]*(N+1)

        for i in range(2,int((N)**0.5)+1):
            if d[i]:
                j=(i)**2
                while j<N+1:
                    d[j]=False
                    j+=i

        d[1],d[0]=False,False

        for i in range(int((N)**0.5),0,-1):
            if N%i==0:
                f1,f2=i,N//i
                if d[f1] and d[f2]:
                    return f1 if f1>f2 else f2
                if d[f1]: return f1
                if d[f2]: return f2
        
class Solution:
    def largestPrimeFactor (self, N):
        i=2
        while i*i<=N:
            if N%i==0:
                N/=i
            else: i+=1
        
        return N
