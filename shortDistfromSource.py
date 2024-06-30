from queue import Queue
class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        if A[0][0]==0: return -1 
        vis=[[False]*M for _ in range(N)]
        q=Queue()
        q.put((0,0,0))
        dx=[-1,0,1,0]
        dy=[0,1,0,-1]
        vis[0][0]=True
        while not(q.empty()):
            cur=q.get()
            if cur[0]==X and cur[1]==Y: return cur[2]
            
            for i in range(4):
                nx=cur[0]+dx[i]
                ny=cur[1]+dy[i]
                if nx>=0 and nx<N and ny>=0 and ny<M and A[nx][ny]==1 and not(vis[nx][ny]):
                    vis[nx][ny]=True
                    q.put((nx,ny,cur[2]+1))
        return -1
