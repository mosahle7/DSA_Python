import math

class Solution:
    
    def merge(self, n, m, arr1, arr2):
        c = math.ceil((m + n) / 2)  # Initial gap size
        le = m + n  # Total length of combined arrays
        
        while c > 0:
            l, r = 0, c  # Set left and right pointers
            
            # Compare elements with the current gap size
            while r < le:
                # Case 1: Both pointers in arr1
                if l < n and r < n:
                    if arr1[l] > arr1[r]:
                        arr1[l], arr1[r] = arr1[r], arr1[l]
                # Case 2: l in arr1, r in arr2
                elif l < n and r >= n:
                    if arr1[l] > arr2[r - n]:
                        arr1[l], arr2[r - n] = arr2[r - n], arr1[l]
                # Case 3: Both pointers in arr2
                elif l >= n and r >= n:
                    if arr2[l - n] > arr2[r - n]:
                        arr2[l - n], arr2[r - n] = arr2[r - n], arr2[l - n]
                
                l += 1
                r += 1
            
            # Update the gap size
            if c == 1:  # If the gap becomes 1, exit the loop after this pass
                break
            c = math.ceil(c / 2)

class Solution:
    
    # Function to merge the arrays.
    def merge(self, n, m, arr1, arr2):
        i, j = n-1, 0
        
        while i>=0 and j<m:
            if arr1[i]>arr2[j]:
                arr1[i],arr2[j]=arr2[j],arr1[i]
                i-=1
                j+=1
            else: break
        
        arr1.sort()
        arr2.sort()
        
