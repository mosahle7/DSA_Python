class Solution:
    def longestConsecutive(self,arr):
        s=set(arr)
        ans=1
        
        for num in arr:
            if num-1 not in s:
                cur = num
                streak = 1
                
                while cur+1 in s:
                    cur = cur+1
                    streak+=1
                ans=max(ans,streak)
        return ans
        
class Solution:
    def longestConsecutive(self,arr):
        ans=1
        arr.sort()
        l=1
        n=len(arr)
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                if i==n-1:
                    ans=max(ans,l)
                continue
            if arr[i]==arr[i-1]+1:
                l+=1
            else:
                ans=max(ans,l)
                l=1
            if i==n-1:
                ans=max(ans,l)
        
        return ans
