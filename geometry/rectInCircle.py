#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        d=2*r
        count = 0
        for i in range(1, d+1):
            for j in range(1, d+1):
                if i*i + j*j <= d**2:
                    count+=1
                    
        return count
                    
        
