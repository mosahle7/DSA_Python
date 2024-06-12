class Solution:
    def countStrings(self,n):
        m=10**9+7
        def multiply(F,M):
            w=((F[0][0]%m*M[0][0]%m)%m+(F[0][1]%m*M[1][0]%m)%m)%m
            x=((F[0][0]%m*M[0][1]%m)%m+(F[0][1]%m*M[1][1]%m)%m)%m
            y=((F[1][0]%m*M[0][0]%m)%m+(F[1][1]%m*M[1][0]%m)%m)%m
            z=((F[1][0]%m*M[0][1]%m)%m+(F[1][1]%m*M[1][1]%m)%m)%m

            F[0][0]=w
            F[0][1]=x
            F[1][0]=y
            F[1][1]=z




        def power(F,n):
            if n==0 or n==1: return
            M=[[1,1],[1,0]]
            power(F,n//2)
            multiply(F,F)
            
            if n%2!=0:
                multiply(F,M)
            

        def fib(n):
            F=[[1,1],
               [1,0]]
            if n==0: return 0

            power(F,n-1)
            return F[0][0]
        
        return fib(n+2)


# class Solution:
#     def generateBinaryStrings(self, n):
#         l=[]
#         def fun(s):
#             if len(s)>1 and s[-2] =='1' and s[-1]=='1': return 0
#             if len(s)==n:
#                 l.append(s)
#                 return
#             fun(s+'0')
#             fun(s+'1')
#             return l
#         return fun('')
# class Solution:
#     def countStrings(self,n):
#         if n==1: return 2
#         if n==2: return 3
#         a,b=2,3

#         for i in range(2,n+1):
#             c=a+b
#             b=c
#             a=b
#         return c

        
