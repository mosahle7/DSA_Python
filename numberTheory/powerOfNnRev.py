class Solution:
    #Complete this function
    def power(self,N,R):
        mod=10**9+7
        
        def fun(n,exp):
            if exp==0: return 1
            
            if exp%2==0:
                ans=fun(n,exp//2)
                ans=ans*ans%mod
            else:
                ans=n%mod
                ans=(ans*fun(n,(exp-1))%mod)%mod
            return ans%mod
        return fun(N,R)%mod
