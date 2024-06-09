class Solution:
    def isPerfectNumber(self, N):
        if N==1 or N==0: return 0
        s=0
        for i in range(2,int(N**0.5)+1):
            if N%i == 0:
                s=s+i+(N//i)
        s+=1
        if s==N: return 1
        return 0
