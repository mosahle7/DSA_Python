class Solution:
    def maxPathSum(self, arr1, arr2):
        n1=len(arr1)
        n2=len(arr2)
        
        i,j=0,0
        s1,s2=0,0
        res=0
        
        while i<=n1-1 and j<=n2-1:
            if arr1[i]<arr2[j]:
                s1+=arr1[i]
                i+=1
            elif arr1[i]>arr2[j]:
                s2+=arr2[j]
                j+=1
            
            else:
                res+=max(s1,s2)
                s1,s2=0,0
                res+=arr1[i]
                i+=1
                j+=1
        
        while i<=n1-1:
            s1+=arr1[i]
            i+=1
            
        while j<=n2-1:
            s2+=arr2[j]
            j+=1
            
        res+=max(s1,s2)
        
        return res
