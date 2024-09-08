class Solution:
	def minJumps(self, arr):
	    n=len(arr)
	    maxReach=0
	    lastInd=0
	    jumps=0
	    
	    if arr[0]==0 and n!=1: return -1
	    
	    for i in range(n):
	        maxReach=max(maxReach,i+arr[i])
	        if i==lastInd:
	            if lastInd==maxReach: return -1
	            lastInd=maxReach
	            jumps+=1
	            if lastInd>=n-1: return jumps
	    return -1
	    
