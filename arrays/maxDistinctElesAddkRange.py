class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        nums[0]-=k
        res=n

        for i in range(1,n):
            if nums[i]+k<nums[i-1]+1:
                nums[i]=nums[i-1]
                res-=1
            else:
                nums[i]=max(nums[i]-k,nums[i-1]+1)
        return res
        
