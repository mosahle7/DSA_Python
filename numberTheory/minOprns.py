class Solution:
    def minOperation(self, n):
        op=0
        num=0
        while num<n:
            if num%2==0: num+=1
            else: num=num*2
            op+=1
        return op
