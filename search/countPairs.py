class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        arr.sort()
        brr.sort()
        
        n=len(arr)
        m=len(brr)
        
        c=0
        
        for i in range(n):
            for j in range(m):
                if arr[i]==1: break
                elif arr[i]!=1 and brr[j]==1: c+=1
                elif arr[i]==2 and brr[j]==3: continue
                elif arr[i]==3 and brr[j]==2: c+=1
                elif arr[i]==2 and brr[j]==4: continue
                elif arr[i]<brr[j]: c+=1
        
        return c



class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        n=len(arr)
        m=len(brr)
        
        brr.sort()
        
        count=[0]*4
        
        for i in range(m):
            if brr[i]==1 or brr[i]==2 or brr[i]==3 or brr[i]==4:
                count[brr[i]-1]+=1
        
        c=0
        
        def upper(ele):
            l,r=0,m-1
            while l<=r:
                mid=(l+r)//2
                
                if brr[mid]<=ele:
                    l=mid+1
                else:
                    r=mid-1
            return l
            
    
        for i in range(n):
            if arr[i]==1: continue
            elif arr[i]==2:
                c+=(m-upper(2))
                c-=count[2]
                c+=count[0]
                c-=count[3]
            
            elif arr[i]==3:
                c+=(m-upper(3))
                c+=count[1]
                c+=count[0]
            
            else:
                c+=(m-upper(arr[i]))
                c+=count[0]
        return c
        
