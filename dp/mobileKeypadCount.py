class Solution:
	def getCount(self, n):
		keypad=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
		dp=[[[-1 for _ in range(n+1)]for _ in range(2+1)]for _ in range(3+1)]
		def solve(i,j,n):
			if i<0 or i>3: return 0
			if j<0 or j>2: return 0
			if keypad[i][j]=='*' or keypad[i][j]=='#': return 0
			if n==1: return 1
			if dp[i][j][n]!=-1: return dp[i][j][n]
		    dp[i][j][n] = solve(i,j,n-1)+solve(i-1,j,n-1)+solve(i,j+1,n-1)+solve(i,j-1,n-1)+solve(i+1,j,n-1)

            return dp[i][j][n]

        c=0
        for i in range(4):
            for j in range(3):
				if keypad[i][j]!='*' or keypad[i][j]!='#':
					c+=solve(i,j,n)


		return c
