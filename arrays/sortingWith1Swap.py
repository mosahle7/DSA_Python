
from typing import List

class Solution:
    def classArrangement(self, n: int, arr: List[int]) -> bool:
        sorted_arr = sorted(arr)
        
        # Find all the indices where the array and the sorted array differ
        diff_indices = [i for i in range(n) if arr[i] != sorted_arr[i]]
        
        # If there are exactly two indices where they differ, check if swapping them would sort the array
        if len(diff_indices) == 2:
            i, j = diff_indices
            arr[i], arr[j] = arr[j], arr[i]
            return arr == sorted_arr
        
        # If there are no differences, the array is already sorted
        # Check if there are duplicates that can be swapped
        if len(diff_indices) == 0:
            seen = set()
            for num in arr:
                if num in seen:
                    return True
                seen.add(num)
            return False
        
        # In all other cases, it's not possible to sort by one swap
        return False
        
