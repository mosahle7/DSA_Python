class Solution:
    def rearrange(self, arr):
        s=set()
        n=len(arr)
        for i in range(n):
            if arr[i]!=-1:s.add(arr[i])
        for i in range(n):
            if i in s: arr[i]=i
            else: arr[i]=-1
        return arr

class Solution:
    def rearrange(self, arr):
        n = len(arr)
        
        # Step 1: Place elements at their correct positions by swapping
        for i in range(n):
            while 0 <= arr[i] < n and arr[i] != arr[arr[i]]:
                # Swap arr[i] with arr[arr[i]] to place it at the correct index
                arr[arr[i]], arr[i] = arr[i], arr[arr[i]]
        
        # Step 2: Mark elements that are not at the correct positions as -1
        for i in range(n):
            if arr[i] != i:
                arr[i] = -1
        
        return arr
