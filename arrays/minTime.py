def minTime(n,li):
    d=[0]*(n)
    l=len(li)
    for i in range(l):
        d[li[i]-1]+=1
    def findEle(val):
        for i in range(n):
            if d[i]==val:
                ind=i
                return ind
    mi=max(d)
    maxi=mi
    mini=min(d)
    minInd=findEle(mini)
    maxInd=findEle(maxi)
    while True:
        d[maxInd],d[minInd]=d[maxInd]-1,d[minInd]+2
        maxi=max(d)
        mini=min(d)
        minInd=findEle(mini)
        maxInd=findEle(maxi)
        if d[maxInd]<=mi: mi=d[maxInd]
        else: break
    return mi
