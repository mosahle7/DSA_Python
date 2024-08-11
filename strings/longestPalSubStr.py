class Solution:
    def longestPalin(self, S):
        m=0
        ans=''
        n=len(S)
        if n==1: return S
        for i in range(n-1):
            
            # checking for odd
            st,end=i,i
            while st>=0 and end<=(n-1) and S[st]==S[end]:
                if (end-st+1)>m:
                    m=end-st+1
                    ans=S[st:end+1]
                    
                st-=1
                end+=1
              
            # checking for even
            st,end=i,i+1
            while st>=0 and end<=(n-1) and S[st]==S[end]:
                if (end-st+1)>m:
                    m=end-st+1
                    ans=S[st:end+1]
                    
                st-=1
                end+=1
                
        return ans
  
