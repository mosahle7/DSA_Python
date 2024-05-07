class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def noSibling(root):
    if root is None:
        return []

    queue = [root]
    d={}
    ind=1
    while queue:
        node = queue.pop(0)
        ind+=1
        if node.left:
            queue.append(node.left)
            if ind//2 in d:
                d[ind//2] = -1

            else:
                d[ind//2]=node.left.data

            
        
        ind+=1
        if node.right:
            queue.append(node.right)
            if ind//2 in d:
                d[ind//2] = -1

            else:
                d[ind//2]=node.right.data

    l=[d[i] for i in d if d[i]!=-1]
    l.sort()
 
    return l if l else [-1]
