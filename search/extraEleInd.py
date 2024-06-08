class Solution:
    def findExtra(self,n,a,b):
        left,right=0,n-1
        while left<right:
            mid=(left+right)//2

            if a[mid]!=b[mid] or mid>len(b)-1:
                right=mid
            else: 
                left=mid+1
        return left


class Solution:
    def findExtra(self,n,a,b):

        for i in range(n):
            if len(a)-1>=i and len(b)-1>=i:
                if a[i]!=b[i]: return i
        return n-1
