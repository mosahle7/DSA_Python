class Solution:
	def matSearch(self, mat, x):
	    n=len(mat)
	    m=len(mat[0])
	    
	    i,j=0,m-1
	    
	    while i<n and j>=0:
	        if mat[i][j]==x:
	            return True
	        elif mat[i][j]>x:
	            j-=1
	        else:
	            i+=1
	    return False
	    
class Solution:
	def matSearch(self, mat, x):
		n=len(mat)
		m=len(mat[0])
		
		def bin(arr):
		    l,r=0,m-1
		    while l<=r:
		        mid=(l+r)//2
		        if arr[mid]==x:
		            return True
		        elif arr[mid]>x:
		            r=mid-1
		        else:
		            l=mid+1
		    return False
		    
		 
		for i in range(n):
		    if x>=mat[i][0] and x<=mat[i][m-1]:
		        c = bin(mat[i])
		        if c:
		            return True
		return False
		    
