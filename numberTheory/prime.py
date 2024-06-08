def prime(n):
    for i in range(2,n):
        isPrime=True
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                isPrime=False
                break
        if isPrime:
            print(i)

def sieveofEratosthenes(n):
    d=[True]*n
    for i in range(2,int(n**0.5)):
        if d[i]:
            j=i**2
            while j<n:
                d[j]=False
                j+=i
    
    ans=0
    for i in range(2,n):
        if d[i]: ans+=1
    return ans

