class Solution:
    
    #Function to find the maximum number of activities that can
    #be performed by a single person.
    def activitySelection(self,n,start,end):
        ar=[]
        for i in range(n):
            a=[]
            a.append(start[i])
            a.append(end[i])
            ar.append(a)
        
        ar.sort(key=lambda x:x[1])
        
        num=0
        day=0
        for i in range(n):
            if ar[i][0]>day and ar[i][1]>day:
                num+=1
                day=ar[i][1]
                
        return num
            
