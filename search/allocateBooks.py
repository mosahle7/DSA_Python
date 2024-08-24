def findPages(arr: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
    if m>n: return -1
    
    s=sum(arr)
    l=max(arr)
    r=s

    if m==n: return l
    if m==1: return s

   

    def countStu(pages):
        stu=1
        stuPages=0
        for i in range(n):
            if stuPages+arr[i]<=pages:
                stuPages+=arr[i]
            else:
                stu+=1
                stuPages=arr[i]
        return stu
    
    # for pages in range(1,r+1):
    #     if countStu(pages)==m:
    #         return pages
    
    while l<=r:
        mid=(l+r)//2
        if countStu(mid)==m:
            r=mid-1
        elif countStu(mid)<m:
            r=mid-1
        else:
            l=mid+1
    
    return l
        

        
