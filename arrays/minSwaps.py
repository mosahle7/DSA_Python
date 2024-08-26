class Solution:
    def minSwaps(self, nums):
        n = len(nums)
        sorted_nums = sorted(nums)
        
        # Create a mapping from value to index in the sorted array
        value_to_index = {value: i for i, value in enumerate(sorted_nums)}
        
        swaps = 0
        visited = [False] * n
        
        for i in range(n):
            # If already visited or already in the correct place
            if visited[i] or nums[i] == sorted_nums[i]:
                continue
            
            # Compute the size of the cycle
            cycle_size = 0
            x = i
            
            while not visited[x]:
                visited[x] = True
                x = value_to_index[nums[x]]
                cycle_size += 1
            
            # Add the number of swaps needed for this cycle
            if cycle_size > 1:
                swaps += (cycle_size - 1)
        
        return swaps

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
	    swaps=0
	    n=len(nums)
	    t=sorted(nums)
	    d={}
	    for i in range(n):
	        d[nums[i]]=i
	        
	    for i in range(n):
	        if nums[i]!=t[i]:
	            swaps+=1
	            ind=d[t[i]]
	            d[t[i]]=i
	            d[nums[i]]=ind
	            nums[i],nums[ind]=nums[ind],nums[i]
	            
	    return swaps
