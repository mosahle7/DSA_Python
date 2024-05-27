def ropeCut(n,a,b,c):
    if n==0: return 0
    if n<0: return -1

    res=max(ropeCut(n-a,a,b,c),ropeCut(n-b,a,b,c),ropeCut(n-c,a,b,c))

    if res == -1: return -1
    return res+1
