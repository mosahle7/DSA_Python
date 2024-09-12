from collections import deque
class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        q=deque()
        t=root
        q.append(t)
        while len(q)!=0:
            cur=q.popleft()
            
            cur.left,cur.right=cur.right,cur.left
            
            if cur.left:
                q.append(cur.left)
            
            if cur.right:
                q.append(cur.right)
                
        return root
