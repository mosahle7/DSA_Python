class Solution:
	def maxProduct(self,arr, n):
		pre,suff=1,1
		m=float('-inf')
		for i in range(n):
		    if pre==0: pre=1
		    if suff==0: suff=1
		    
		    pre*=arr[i]
		    suff*=arr[n-1-i]
		    m=max(m,pre,suff)
		return m
		
    def maxProduct(self,arr,n):
        maxSoFar=arr[0]
        minSoFar=arr[0]
        maxEnd=arr[0]
        for i in range(1,n):
            if arr[i]<0:
                maxEnd,minSoFar=minSoFar,maxEnd
            maxEnd=max(maxEnd*arr[i],arr[i])
            minSoFar=min(minSoFar*arr[i],arr[i])
            maxSoFar=max(maxSoFar,maxEnd)
        
        return maxSoFar
