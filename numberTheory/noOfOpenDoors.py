class Solution:
    def noOfOpenDoors(self, N):
        return int(N**0.5)

class Solution:
    def noOfOpenDoors(self, N):
        o=0
        def factors(n):
            f=0
            for i in range(1,int(n**0.5)+1):
                if i*i==n: f+=1
                elif n%i==0: f+=2
            return f

        for i in range(1,N+1):
            if factors(i)%2!=0: o+=1
        return o
