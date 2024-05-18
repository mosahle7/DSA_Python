def grayCode(n):
    if n== 0:
        return [0]
    
    res = [0,1]
    for i in range(2,n+1):
        ref = res[::-1]
        res+=[x + (1<<(i-1)) for x in ref]
    return res

def grayCodeBin(n):
    grayCodes = grayCode(n)
    return [bin(x)[2:].zfill(n) for x in grayCodes]
print(grayCodeBin(4))
