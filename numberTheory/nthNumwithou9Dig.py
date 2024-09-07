
class Solution:
    def findNth(self,n):
        if n<9: return n
        
        def contains9(num):
            while num>0:
                if num%10==9: return True
                num=num//10
            
            return False
        
        c=0
        for i in range(1,n+1):
            if contains9(i): c+=1
        
        ans=n+c
        while contains9(ans):
            ans+=1
        return ans

class Solution:
    def findNth(self, n):
        result = 0
        multiplier = 1
        while n>0:
            result+=(n%9)*multiplier
            n=n//9
            multiplier*=10
        return result
