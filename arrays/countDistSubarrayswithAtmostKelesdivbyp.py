from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        subarrays = set()

        # Iterate over all possible starting points of the subarray
        for i in range(n):
            count_divisible = 0
            
            # Use a sliding window starting from index i
            for j in range(i, n):
                # Count the number of elements divisible by p
                if nums[j] % p == 0:
                    count_divisible += 1

                # If the count exceeds k, break the inner loop
                if count_divisible > k:
                    break

                # Convert the current subarray slice to a tuple and add to the set
                subarrays.add(tuple(nums[i:j+1]))
        
        return len(subarrays)
