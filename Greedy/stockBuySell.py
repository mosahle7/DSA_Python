class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr, n):
		ans=[]
		i=0
		p=0
		buy,sell=None,None
		while i<=n-1:
		    if p%2==0:
		        if i==n-1:
		            break
		        elif arr[i+1]>=arr[i]:
		            buy=i
		            p+=1
		    else:
		        if i==n-1:
		            sell=i
		            
		        elif arr[i+1]<=arr[i]:
		            sell=i
		            p+=1
		    if buy is not None and sell is not None:
		        ans.append((buy,sell))
		        buy=None
		        sell=None
		  
		    i+=1
		return ans
