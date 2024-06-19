import math
class Solution:
    def maxVolume(self, per, ar):
        sqr=math.sqrt(per**2-24*ar)
        l=(per-sqr)/12
        ans=l*l*((per/4)-2*l)
        return ans
