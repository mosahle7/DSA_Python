def lexSmall(S):
    r=S[1:]
    b=S[0]
    k=''
    l=len(S)
    strs=[]
    memo={}
    def fun(r,b,k):
        if (r,b,k) in memo:
            return memo[(r,b,k)]

        if len(r)==0 and len(b) == 0:
            result=[k]
        else: 
            result=[]
            if len(r)!=0:
                result.extend(fun(r[1:],b+r[0],k))
            if len(b)!=0:
                result.extend(fun(r,b[:-1],k+b[-1]))
            
        memo[(r,b,k)]= result
        return result
    return min(fun(r,b,k))
    
