class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        if n==0: return 0
        dp=[1]*(n)
        for i in range(1,n):
            for j in range(i):
                if a[i]>a[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
       

#User function Template for python3


class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        def binSearch(s,ele):

            l,r=0,len(s)-1
            
            while l<r:
                mid=(l+r)//2
                
                if s[mid]>=ele:
                    r=mid
                else:
                    l=mid+1
            return l
        
        s=[]
        s.append(a[0])
        for i in range(1,n):
            if a[i]>s[-1]:
                s.append(a[i])
              
            else:
                ind=binSearch(s,a[i])
                s[ind]=a[i]
               
        return len(s)


#User function Template for python3


class Solution:
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self, n, a):
        def binSearch(s,ele):

            l,r=0,len(s)-1
            
            while l<r:
                mid=(l+r)//2
                
                if s[mid]>=ele:
                    r=mid
                else:
                    l=mid+1
            return l
        
        s=[]
        s.append(a[0])
        for i in range(1,n):
            if a[i]>s[-1]:
                s.append(a[i])
              
            else:
                ind=binSearch(s,a[i])
                s[ind]=a[i]
               
        return len(s)


