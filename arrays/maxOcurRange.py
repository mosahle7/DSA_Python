
class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        d={}
        for i in range(maxx+1):
            d[i]=0
        
        for i in range(n):
            for j in range(l[i],r[i]+1):
                d[j]+=1
        
        m=float('-inf')
        n=float('inf')

        for i in range(maxx+1):
            if d[i]>=m: 
                m=d[i]

        for i in range(maxx+1):
            if d[i]==m: 
                if n>i: n=i
        return n
            
# n = 5
# l= [1,5,9,13,21]
# r = [15,8,12,20,30]
# maxx = 30
# ob=Solution()
# print(ob.maxOccured(n,l,r,maxx))

class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        d=[0]*(maxx+2)
        
        for i in range(n):
            d[l[i]]+=1
            d[r[i]+1]-=1
        
        m=float('-inf')
        res=float('inf')
        for i in range(1,maxx+1):
            d[i]+=d[i-1]
            if m<d[i]: 
                m=d[i]
                res=i
        return res

# n = 3
# l= [1,2,3]
# r = [3,5,7]
# maxx = 7
# ob=Solution()
# print(ob.maxOccured(n,l,r,maxx))

            

