class Solution:
    def wordBreak(self, n, s, diction):
        l=len(s)
        d=set()
        dp=[-1]*(l+1)
        for i in range(n):
            d.add(diction[i])
        
        def fun(i,st):
            if i==l: return 1
            if st in d: return 1
            if dp[i]!=-1: return dp[i]
            
            sub=''
            for j in range(i,l):
                sub+=st[j]
                if sub in d and fun(j+1,st)==1:
                    dp[i]=1
                    return dp[i]
            dp[i]=0
            return dp[i]
        return fun(0,s)
