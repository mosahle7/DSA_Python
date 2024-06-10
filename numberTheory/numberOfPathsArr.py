class Solution:
    def numberOfPaths(self, M, N):
        def modInv(n,mod):
            return (pow(n,mod-2,mod))
        
        ans=1
        mod=10**9+7
        for i in range(N,(N+M-1)):
            ans=(ans*i)%mod
            inv=modInv(i-N+1,mod)
            ans=(ans*inv)%mod

        return ans    
    
