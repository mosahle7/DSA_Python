class Solution:
    def smithNum(self, n):
        if n==2: return 0
        pfSum=0
        # fact=[]
        def sumDig(temp):
            i=1
            dSum=0
            while temp>0:
                dSum+=temp%(10)
                temp=temp//(10)
                i+=1
            return dSum
     
        temp=n
        dSum=sumDig(temp)
        
        while n%2==0:
            pfSum+=2
            # fact.append(2)
            n=n//2


        for i in range(3,int(n**0.5)+1,2):
            while n!=2 and n%i==0:
                if i<10:
                    # fact.append(i)
                    pfSum+=i
                else:
                    # fact.append(i)
                    pfSum+=sumDig(i)
                n=n//i
        if n==temp: return 0
        if n>2: 
            pfSum+=sumDig(n)
            # fact.append(n)
            
        # return dSum,pfSum,temp,fact
        return 1 if pfSum==dSum else 0
