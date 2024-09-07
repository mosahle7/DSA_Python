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
                    
