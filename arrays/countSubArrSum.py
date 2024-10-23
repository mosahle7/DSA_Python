
class Solution:
    def subArraySum(self,arr,k):
        s={0:1}
        n=len(arr)
        curS=0
        c=0
        for i in range(n):
            curS+=arr[i]
            
            if curS-k in s:
                c+=s[curS-k]
             
            if curS in s:
                s[curS]+=1
            else:
                s[curS]=1
            
        return c
