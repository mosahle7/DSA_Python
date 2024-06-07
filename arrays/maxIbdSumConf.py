def brMax_sum(a,n):
    ans=0
    for i in range(n):
        su=0
        for j in range(n):
            su+=j*a[(i+j)%n]
        
        if su>ans: ans=su
    return ans

def omMax_sum(a,n):
    su=0
    prevSum=0
    for i in range(n):
        prevSum+=(i*a[i])
        su+=a[i]
    
    ans=prevSum
    for i in range(1,n):
        curSum=prevSum-(sum-a[i-1])+a[i-1]*(n-1)

        prevSum=curSum
        if curSum>ans: ans=curSum
    return ans

a=[8,3,1,2]
n=4
print(max_sum(a,n))
