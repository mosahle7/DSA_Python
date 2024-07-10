class Solution:
    def threeSumClosest (self, arr, tar):
        n=len(arr)
        arr.sort()
        su=(float('-inf'),float('inf'))
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                s=arr[i]+arr[l]+arr[r]
                if s==tar:
                    return s
                if abs(s-tar)<su[1]:
                    su=(s,abs(s-tar))
            
                elif abs(s-tar)==su[1]:
                    if s>su[0]:
                        su=(s,abs(s-tar))

                
                if s>tar:
                    r-=1
                
                else: 
                    l+=1
                
        return su[0]
