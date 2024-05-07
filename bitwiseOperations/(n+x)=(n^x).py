def countNums(n):

    unsetBits=0

    while n:
        if n&1 == 0:
            unsetBits+=1
    
        n>>=1
    return (1<<unsetBits)  # 2^(no of unset bits0
