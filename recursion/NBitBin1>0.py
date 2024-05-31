class Solution:
	def NBitBinary(self, n):
		res=[]
		def fun(n,cur,co,cz):
			if n==0: 
				res.append(cur)
				return
			fun(n-1,cur+'1',co+1,cz)
			if co>cz:
				fun(n-1,cur+'0',co,cz+1)
	    fun(n,'',0,0)
		return res
