class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def Paths(self, root):
        l=[]
        self.findPaths(root,[],l)
        return l
    def findPaths(self,root,path,l):

        if not root:
            return

        path.append(root.data)
        if not(root.left or root.right):
            l.append(path[:])
        else:
            self.findPaths(root.left,path,l)
            self.findPaths(root.right,path,l)

        path.pop()
