class Node:
        def __init__(self, data):
            self.data = data
            self.left = self.right = None

#Function to return a tree created from postorder and inoreder traversals.


class Solution:
    def buildTree(self, In, post, n):
        # Base case: If the number of nodes is 0, return None
        if n == 0:
            return None
        
        # Find the root node using the last element of the postorder traversal
        root = Node(post[n - 1])
        
        # Find the index of the root node in the inorder traversal
        rootIndex = In.index(post[n - 1])
        
        # Recursively build left and right subtrees
        root.left = self.buildTree(In, post, rootIndex)
        root.right = self.buildTree(In[rootIndex + 1:], post[rootIndex:n - 1], n - 1 - rootIndex)
        
        return root






    


    
