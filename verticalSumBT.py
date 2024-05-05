class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Complete the function below
    
    def verticalSum(self, root):
        l={}

        def pre(root,level):
            if root!=None:

                if level not in l:
                    l[level]=root.data
                else:
                    l[level]+=root.data

                pre(root.left,level-1)
                pre(root.right,level+1)
        
        pre(root,0)
            

        return [l[k] for k in sorted(l.keys())]
