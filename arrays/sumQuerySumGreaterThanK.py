from typing import List

class Solution:
    def BiggerFind(self, n : int, arr : List[int], q : int, que : List[List[int]]) -> List[int]:
        

        def segTree(ind,st,end,ans,thr):
            if st==end: 
                if arr[st]>=thr:
                    ans[ind]=arr[st]
                return 

            mid=(st+end)//2

            segTree(2*ind+1,st,mid,ans,thr)
            segTree(2*ind+2,mid+1,end,ans,thr)

            ans[ind]=(ans[2*ind+1]+ans[2*ind+2])

        def query(ind,st,end,qs,qe):

            if qs>end or qe<st:
                return 0
    
            if qs<=st and qe>=end:
                return ans[ind]
    
            mid=(st+end)//2

            l=query(2*ind+1,st,mid,qs,qe)
            r=query(2*ind+2,mid+1,end,qs,qe)

            return (l+r)
        
        res=[]
        
        for i in range(q):
            thr=que[i][2]
            qs,qe=que[i][0],que[i][1]
            ans=[0 for _ in range(4*n)]
            segTree(0,0,n-1,ans,thr)
            res.append(query(0,0,n-1,qs,qe))
        
        return res
            
            
        
        
        
class Solution:
    def BiggerFind(self, n : int, A : List[int], q : int, queries : List[List[int]]) -> List[int]:
        res=[]
        for i in range(q):
            l,r=queries[i][0],queries[i][1]
            co=queries[i][2]
            su=0
            while l<=r:
                if l==r: 
                    if A[l]>=co: su+=A[l]
                else:
                    if A[l]>=co: su+=A[l]
                    if A[r]>=co: su+=A[r]
                l+=1
                r-=1
            res.append(su)
        return res
            
