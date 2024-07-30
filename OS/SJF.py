import heapq

def SJF(n, at, bt):
    t=0
    pro=[]
    for i in range(n):
        pro.append([at[i],bt[i],i+1])
    
    pro.sort()
    cpu=[]
    minHeap=[]

    t=pro[0][0]
    heapq.heappush(minHeap, [pro[0][1],pro[0][2]])
    ind=1

    while len(cpu)<n:

        while ind<n and pro[ind][0]<=t:
            heapq.heappush(minHeap, [pro[ind][1],pro[ind][2]])
            ind+=1

        if minHeap:
            c=heapq.heappop(minHeap)
            t+=c[0]
            cpu.append(c[1])
            
        else:
            if ind<n:
                t=pro[ind][0]
                heapq.heappush(minHeap,[pro[ind][1],pro[ind][2]])
                ind+=1

    return cpu,t

n=4
at=[0,1,2,3]
bt=[8,4,9,5]
print(SJF(n,at,bt))

def SJF(n,at,bt):
    t=0
    pro=[]
    for i in range(1,n):
        pro.append([i+1,at[i],bt[i]])
    pro.sort(key= lambda x: x[2])
    cpu=[]
    cpu.append(1)
    t+=bt[0]
    s=set()
    while len(cpu)!=n:
        for i in range(len(pro)):
            if pro[i][1]<=t and i not in s:
                s.add(i)
                cpu.append(pro[i][0])
                t+=pro[i][2]
                break
    
    return cpu,t
