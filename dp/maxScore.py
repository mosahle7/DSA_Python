class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n=len(b)
        memo={}
        def fun(ia,ib):
            if (ia,ib) in memo: return memo[(ia,ib)]
            if ia==4: return 0
            if ib==n: return float('-inf')
            
            memo[(ia,ib)]=max(fun(ia,ib+1),fun(ia+1,ib+1)+a[ia]*b[ib])
            return memo[(ia,ib)]
        return fun(0,0)

class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        n=len(b)
        dp=[[float('-inf')]*(n+1) for _ in range(5)]
        
        for i in range(n+1):
            dp[4][i]=0
        
        for i in range(3,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j]=max(dp[i][j+1],dp[i+1][j+1]+a[i]*b[j])
        return dp[0][0]


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        # Initialize the variables to store the maximum score for each step
        dp1 = dp2 = dp3 = dp4 = -float('inf')
        
        # Iterate over the array b
        for x in b:
            # Update the dp variables in reverse order
            dp4 = max(dp4, dp3 + a[3] * x)  # Maximize a[0]*b[i0] + a[1]*b[i1] + a[2]*b[i2] + a[3]*b[i3]
            dp3 = max(dp3, dp2 + a[2] * x)  # Maximize a[0]*b[i0] + a[1]*b[i1] + a[2]*b[i2]
            dp2 = max(dp2, dp1 + a[1] * x)  # Maximize a[0]*b[i0] + a[1]*b[i1]
            dp1 = max(dp1, a[0] * x)        # Maximize a[0]*b[i0]

        # The final result is stored in dp4
        return dp4
