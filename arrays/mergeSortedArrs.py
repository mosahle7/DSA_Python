import math
class Solution:
    def mergeArrays(self, arr1, arr2):
        n=len(arr1)
        m=len(arr2)
        
        def next_gap(gap):
            if gap<=1: 
                return 0
            return math.ceil(gap/2)
        
        gap=next_gap(m+n)
        
        while gap>0:
            i=0
            while gap+i<n:
                if arr1[i]>arr1[i+gap]:
                    arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
                i+=1
                
            j=max(0,gap-n)
            
            while i<n and j<m:
                if arr1[i]>arr2[j]:
                    arr1[i],arr2[j]=arr2[j],arr1[i]
                i+=1
                j+=1
            
            j=0
            while gap+j<m:
                if arr2[j]>arr2[j+gap]:
                    arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
                j+=1
                
            gap=next_gap(gap)

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
        
