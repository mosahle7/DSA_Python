class Solution:
    def kPangram(self,str, k):
        d={}
        if len(str)<26: return False
        numL=0
        for i in str:
            if i.isalpha():
                numL+=1
                if i not in d:
                    d[i]=1
                else:
                    d[i]+=1
        
        if numL<26: return False 
        
        diff=0
        l=len(d)
        req=26-l
        if req<=0: return True 
        
        return True if req<=k else False
        
