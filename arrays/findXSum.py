from sortedcontainers import SortedList

class Solution:
    def findXSum(self, A: List[int], K: int, X: int) -> List[int]:
        n=len(A)
        top=SortedList()
        bot=SortedList()
        count=Counter()
        curS=0
        ans=[]

        def update(x,qty):
            nonlocal curS
            if count[x]:
                try:
                    bot.remove([count[x],x])
                except:
                    top.remove([count[x],x])
                    curS-=(x*count[x])
            
            count[x]+=qty
            if count[x]:
                bot.add([count[x],x])
        
        for i in range(n):
            update(A[i],1)
            if i>=K:
                update(A[i-K],-1)
            
            while bot and len(top)<X:
                cx,x=bot.pop()
                top.add([cx,x])
                curS+=(x*cx)
            
            while bot and bot[-1]>top[0]:
                cx,x=bot.pop()
                cy,y=top.pop(0)
                curS+=(cx*x-cy*y)
                top.add([cx,x])
                bot.add([cy,y])
            
            if i>=K-1:
                ans.append(curS)
        return ans
