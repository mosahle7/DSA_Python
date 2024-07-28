class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        ans=0
        prefix=[0]*n
        for i in range(n):
            if s[i]=='1':
                prefix[i]=1
        
        for i in range(1,n):
            prefix[i]+=prefix[i-1]

        for i in range(n):
            ones=0
            zeros=0
            j=i
            while j<n:
                ones=prefix[j]
                if i!=0:
                    ones-=prefix[i-1]
                zeros=j-i+1-ones

                if zeros**2>ones:
                    j+=(zeros**2-ones-1)

                if zeros**2<=ones:
                    ans+=1

                    if zeros**2<ones:
                        diff=int(sqrt(ones))-zeros
                        nextj=j+diff

                        if nextj>=n:
                            ans+=(n-1-j)
                        else:
                            ans+=diff
                        
                        j=nextj
                j+=1
        return ans
