def checkAllSet(n):

    if n&(n+1) == 0:
        return True
    return False

def Alt(n):

    if checkAllSet(n^(n>>1)):
        return True
    
    return False
