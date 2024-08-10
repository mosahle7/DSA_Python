class Solution:
    def editDistance(self, s1, s2):  
        memo={}
        def fun(s1,s2):
            if (s1,s2) in memo:
                return memo[(s1,s2)]
    
            
            if not(s1):
                return len(s2)
        
            if not(s2): 
                return len(s1)
            
            if s1[-1]==s2[-1]:
                memo[(s1,s2)] = fun(s1[:-1],s2[:-1])
            
            else:
                memo[(s1,s2)]=1+min(fun(s1,s2[:-1]), fun(s1[:-1],s2[:-1]), fun(s1[:-1],s2))
            return memo[(s1,s2)]
        
        return fun(s1,s2)  
        

s1="abc"
s2="adc"
ob=Solution()
print(ob.editDistance(s1,s2))

class Solution:
    def editDistance(self, s1, s2): 
        m,n=len(s1),len(s2) 
        dp=[[0]* (n+1) for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0]=i
        for i in range(n+1):
            dp[0][i]=i
            
        for i in range(1,m+1):
            for j in range(n+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    
        return dp[m][n]
        
