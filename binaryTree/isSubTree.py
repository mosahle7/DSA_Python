from collections import deque
class Solution:
    def isSubTree(self, T, S):
        q=deque()
        q.append(T)
        
        while len(q)!=0:
            cur=q.popleft()
            if cur.data==S.data:
                t=cur
                s=deque()
                s.append((t,S))
                comp=True
                
                while len(s)!=0:
                    t,p=s.popleft()
                    if t.left:
                        if p.left is None:
                            comp=False    
                            break
                        if t.left.data==p.left.data:
                            s.append((t.left,p.left))
                        else:
                            comp=False
                            break
                    elif p.left and t.left is None:
                        comp=False    
                        break
                    
                    if t.right:
                        if p.right is None:
                            comp=False    
                            break
                        if t.right.data==p.right.data:
                            s.append((t.right,p.right))
                        else:
                            comp=False
                            break
                    elif p.left and t.left is None:
                        comp=False    
                        break
                if comp==True: return True
                
                
            if cur.left:
                q.append(cur.left)
            
            if cur.right: 
                q.append(cur.right)
        return False

class Solution:
    def isSubTree(self, T, S):
        if not S:  # An empty tree is always a subtree
            return True
        if not T:  # If T is empty and S is not, S can't be a subtree
            return False

        # If the roots of T and S are the same, check if the subtrees are identical
        if self.areIdentical(T, S):
            return True

        # Otherwise, continue checking the left and right subtrees of T
        return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)

    def areIdentical(self, T, S):
        # If both nodes are None, they're identical
        if not T and not S:
            return True
        # If one of the nodes is None but the other isn't, they're not identical
        if not T or not S:
            return False
        # If the values of T and S are different, they're not identical
        if T.data != S.data:
            return False

        # Check if the left and right subtrees are also identical
        return self.areIdentical(T.left, S.left) and self.areIdentical(T.right, S.right)

            
