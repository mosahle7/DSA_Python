
class Solution:
    def waysToBreakNumber(self, n):
        m=10**9+7
        return (((n+1)%m*(n+2)%m)//2)%m
