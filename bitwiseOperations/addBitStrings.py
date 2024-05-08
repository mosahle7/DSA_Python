def addBitStrings(str1,str2):

    result = ''

    def makeEqaulLen(str1,str2):
        l1,l2=len(str1),len(str2)

        if l1>l2:
            str2=(l1-l2)*'0'+str2
        elif l2>l1:
            str1+=(l2-l1)*'0'+str1
        
        return l1,str1,str2

    l,str1,str2=makeEqaulLen(str1,str2)        
    carry=0

    for i in range(l-1,-1,-1):
        fBit,sBit=int(str1[i]),int(str2[i])
        sum=fBit^sBit^carry
        result = chr(sum+48) + result

        carry = (fBit&sBit) | (fBit&carry) | (sBit&carry) 

    if carry == 1:
        result ='1'+result
    return result
