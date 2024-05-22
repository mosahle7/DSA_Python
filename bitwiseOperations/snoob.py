def snoob(n):
    rightOne = n&-n
    higherOneBit = n+rightOne

    rightOnePattern = n^int(higherOneBit)
    rightOnePattern = int(rightOnePattern)/int(rightOne)
    rightOnePattern = int(rightOnePattern)>>2

    next = higherOneBit | rightOnePattern

    return next
