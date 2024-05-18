class Solution:
	def findPeakElement(self, a):
		low,high = 0,len(a)-1
		while low<high:
			mid = (low+high)//2
			if a[mid]>a[mid+1]:
				high = mid
			else:
				low=mid+1
		return a[low]
