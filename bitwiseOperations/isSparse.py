class Solution:
    def isSparse1(self,n):
        c=0
        while n!=0:
            if n&1:
                c+=1
                if c==2:
                    return 1
            else:
                c=0

    def isSparse2(self,n):
        if (n&(n>>1)):
            return 0
        return 1
    

                 

