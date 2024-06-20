
class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        s=sum(a)
        dp=[-1]*n
        def fun(ind):
            if ind>n-1: return 0
            if dp[ind]!=-1: return dp[ind]
            dp[ind]= max(fun(ind+2)+a[ind],fun(ind+1))
            return dp[ind]
        return fun(0)

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,a, n):
        s=sum(a)
        dp=[0]*(n+1)
        for i in range(1,n+1):
            dp[i]=max(dp[i-2]+a[i-1],dp[i-1])
        return dp[n]
        # code here

class Solution:  
    
    #Function to find the maximum money the thief can get.
    def FindMaxSum(self,arr, n):
        a=0
        b=arr[0]
        for i in range(2,n+1):
            c=max(arr[i-1]+a,b)
            a=b
            b=c
        return c
