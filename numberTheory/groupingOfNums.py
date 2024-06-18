class Solution:
    def maxGroupSize(self, arr, N, K):
        rem=[0]*(K)
        for i in range(N):
            rem[arr[i]%K]+=1
        
        ans=0
        for k in range(0,(K//2)+1):
            if (k==0 or k==K-k):
                if rem[k]!=0:
                    ans+=1
            else:
                ans+=max(rem[k],rem[K-k])
        
      
        return ans
            
