class Solution:
	def mergeOverlap(self, arr):
		arr.sort()
		n=len(arr)
		idx=0
		for i in range(1,n):
		    if arr[i][0]<=arr[idx][1]:
		            arr[idx][1]=max(arr[idx][1],arr[i][1])
		    else:
		        idx+=1
		        arr[idx]=arr[i]
		return arr[:idx+1]



class Solution:
	def overlappedInterval(self, inters):
	    inters.sort()
	    n=len(inters)
        
        ans=[]
        i=0
        while i<n:
            st=inters[i][0]
            end=inters[i][1]
            i+=1
    
            while i<n:
                if inters[i][0]>end:
                    ans.append([st,end])
                    break
                else:
                    if inters[i][1]>end:
                        end=inters[i][1]

                i+=1
            if i==n: ans.append([st,end])
            
        return ans
                    
