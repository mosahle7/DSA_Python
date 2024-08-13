class Solution:
    def matrixMultiplication(self, N, arr):
        memo={}
        def fun(i,j):
            if (i,j) in memo: return memo[(i,j)]
            if i==j: return 0
            mi=float('inf')
            
            for k in range(i,j):
                steps=arr[i-1]*arr[k]*arr[j]+fun(i,k)+fun(k+1,j)
            
                if steps<mi: mi=steps 
            
            memo[(i,j)]=mi
            return memo[(i,j)]
            
        return fun(1,N-1)
            
