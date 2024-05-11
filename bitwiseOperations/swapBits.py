class Solution:
    def swapBits1(self, X, P1, P2, N):
        binNum=bin(X)
        binN=binNum[2:]
        l=len(binN)
        res=''
        
        ind1=l-1-P1-(N-1)
        ind2=l-1-P2-(N-1)

        if not(l-1-P1-(N-1) <0 and l-1-P2-(N-1)<0):
            s1=binN[l-1-P1-(N-1):l-1-P1+1]
            s2=binN[l-1-P2-(N-1):l-1-P2+1]
            res=binN[0:l-1-P2-(N-1)]+binN[l-1-P1-(N-1):l-1-P1+1]+binN[l-1-P2+1:l-1-P1-(N-1)]+binN[l-1-P2-(N-1):l-1-P2+1]+binN[l-1-P1+1:l]
            l=len(binN)

        if  l-1-P2-(N-1)<0:
            binN=('0'*(-(l-1-P2-(N-1)))) +binN
            dif=-(l-1-P2-(N-1))
            res=binN[0+dif:l-1-P2-(N-1)+dif]+binN[l-1-P1-(N-1)+dif:l-1-P1+1+dif]+binN[l-1-P2+1+dif:l-1-P1-(N-1)+dif]+binN[l-1-P2-(N-1)+dif:l-1-P2+1+dif]+binN[l-1-P1+1+dif:l+dif]

        return int(res,2)

    def swapBits2(self,X,P1,P2,N):
        set1 = (X>>P1) & ((1<<N)-1)
        set2=  (X>>P2) & ((1<<N)-1)

        xor = set1^set2

        xor = (xor<<P1) | (xor<<P2)

        res=xor ^ X

        return res

