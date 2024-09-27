from collections import deque

class Solution:
    
    # Function to find the maximum of each subarray of size k.
    def max_of_subarrays(self, k, arr):
        n=len(arr)
        d=deque()
        ans=[]
        
        for i in range(n):
            if dq and dq[0]==i-k:
                dq.popleft()
                
            while dq and arr[dq[-1]]<arr[i]:
                dq.pop()
                
            dq.append(i)
            
            if i<=k-1:
                ans.append(arr[dq[0]])
        return ans
