
from queue import Queue
class Solution:
    def steppingNumbers(self, n, m):
        def bfs(n,m,st):
            q=Queue()
            q.put(st)
            k=0
            while not(q.empty()):
                x=q.get()
                if n<=x<=m:
                    k+=1
                if x==0 or x>m: continue
                
                lastDig=x%10
                a=x*10+lastDig+1
                b=x*10+lastDig-1
                
                if lastDig==0:
                    q.put(a)
                elif lastDig==9:
                    q.put(b)
                else:
                    q.put(a)
                    q.put(b)
            return k

class Solution:
    def steppingNumbers(self, n, m):
        def dfs(n,m,i):
            k=0
            if n<=i<=m: k+=1
            if i==0 or i>m: return k
            
            lastD=i%10
            a=i*10+lastD+1
            b=i*10+lastD-1
            if lastD==0:
                k+=dfs(n,m,a)
            elif lastD==9:
                k+=dfs(n,m,b)
            else: 
                k+=dfs(n,m,a)
                k+=dfs(n,m,b)
            return k
                
        c=0
        for i in range(10):
            c+=dfs(n,m,i)
        return c
                
