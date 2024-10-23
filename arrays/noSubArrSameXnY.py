class Solution:
    def sameOccurrence(self, arr, x, y):
        n = len(arr)
        balance = 0
        count = 0
        freq = {0: 1}  # Initialize with 0 balance count as 1 (to handle subarrays from the start)

        for i in range(n):
            # Update balance based on whether arr[i] is x or y
            if arr[i] == x:
                balance += 1
            elif arr[i] == y:
                balance -= 1
            
            # If the balance has been seen before, add the count of such occurrences to the result
            if balance in freq:
                count += freq[balance]
            
            # Update the frequency of the current balance
            if balance in freq:
                freq[balance] += 1
            else:
                freq[balance] = 1
        
        return count
