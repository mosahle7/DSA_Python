import heapq
class Solution:
    def minTimeToReach(self, move: List[List[int]]) -> int:
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]

        h=[(0,(0,0))]
        n=len(move)
        m=len(move[0])

        time=[[float('inf')]* m for _ in range(n)]
        time[0][0]=0

        def isSafe(x,y):
            return 0<=x<n and 0<=y<m
        while h:
            t,node=heapq.heappop(h)
            if node == (n-1,m-1):
                return time[n-1][m-1]
            x,y=node
            for k in range(4):
                nx=x+dx[k]
                ny=y+dy[k]

                if isSafe(nx,ny):
                    newT=t
                    if move[nx][ny]<=t:
                        newT+=1
                    else:
                        newT=move[nx][ny]+1
                    if newT<time[nx][ny]:
                        time[nx][ny]=newT
                        heapq.heappush(h,(newT,(nx,ny)))
            
