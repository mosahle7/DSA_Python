class Solution:
    def twoSum(self, arr, target):
        # Dictionary to store the frequency of each element
        freq = {}
        
        for num in arr:
            complement = target - num
            # Check if the complement exists in the hashmap
            if complement in freq:
                # If the complement is the same as the current number,
                # ensure there are at least two occurrences
                if complement != num or freq[complement] > 0:
                    return True
            # Add or update the current number in the hashmap
            freq[num] = freq.get(num, 0) + 1
        return False
