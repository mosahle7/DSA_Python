
class Solution:
    def minLength(self, s: str, num: int) -> int:
        n=len(s)
        def minMoves1(s):
            res1,res2=0,0
            n=len(s)
            for i in range(n):
                if i&1:
                    if s[i]=='0':
                        res1+=1
                    else:
                        res2+=1
                else:
                    if s[i]=='0':
                        res2+=1  
                    else:
                        res1+=1
            return min(res1,res2)
        
        def minMoves(s,x):
            b = s[0]
            l = 1
            m=0
            for i in range(1,n):
                if s[i]==b:
                    l+=1
                else:
                    m+=l//(x+1)
                    b=s[i]
                    l=1
                if i==n-1:
                    m+=l//(x+1)
            return m

        if minMoves1(s)<=num:
            return 1
        l,r = 2,n

        while l<r:
            mid=(l+r)//2

            if minMoves(s,mid)>num:
                l=mid+1
            else:
                r=mid
        return l

            
                    
                
