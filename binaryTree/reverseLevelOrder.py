class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):

    if not root:
        return []

    queue=[root]
    res=[]
    while queue:

        levelSize=len(queue)
        levelNodes=[]
        

        for i in range(levelSize):
            current=queue.pop(0)
            levelNodes.append(current.data)

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)

        res.append(levelNodes)
        l=res[::-1]
        m=[]
        for i in l:
            for j in range(len(i)):
                m.append(i[j])

    return m

