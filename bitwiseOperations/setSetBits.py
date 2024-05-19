class Solution:
    def setSetBit(self, x, y, l, r):
        l-=1
        r-=1
        mask = ((1<<(r-l+1))-1)<<1
        bitsToSet = y&mask
        x|=bitsToSet
        return x

  class Solution:
    def setSetBit(self, x, y, l, r):
        m=max(x.bit_length(),y.bit_length())
        
        for i in range(m-1-r,m-l):
            if (y&1<<i):
                bmask = 1<<i
                x=x|bmask
        return x
