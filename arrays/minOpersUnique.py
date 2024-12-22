                
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans=0
        while len(nums)>len(set(nums)):
            nums = nums[3:]
            ans+=1
        return ans
            

from collections import defaultdict
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n=len(nums)
        d=defaultdict(int)
        ans=0
        
        for i in range(n):
            d[nums[i]]+=1

        def check(di):
            for k in di:
                if di[k]>1:
                    return True
            return False
            
        ind=-1

        if not(check(d)):
            return ans
            
        while ind<n:
            for j in range(ind+1,ind+4):
                d[nums[j]]-=1
                ind=j
                if j==n-1:
                    break
            ans+=1
            if not(check(d)):
                return ans
