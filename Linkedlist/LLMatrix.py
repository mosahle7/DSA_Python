class Solution:
    def constructLinkedMatrix(self, mat):
        n=len(mat)
        c=0
        i=0
        j=0
        while c<n*n:
            if i==0 and j==0:
                head=Node(mat[0][0])
                c+=1
                t=head
                cur=head
                if j==n-1:
                    j=0
                    i+=1
                else:
                    j+=1
            else:
                newNode=Node(mat[i][j])
                c+=1
                if j==0:
                    k=t
                    k.down=newNode
                    k=k.right
                    t=newNode
                    cur=t
                    j+=1
                else:
                    cur.right=newNode
                    cur=newNode
                    if i>0:
                        k.down=cur
                        k=k.right
                    if j==n-1:
                        j=0
                        i+=1
                    else:
                        j+=1
        return head

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class Solution:
    def constructLinkedMatrix(self, mat):
        n = len(mat)
        head = Node(mat[0][0])  # Create the head node
        row_heads = [None] * n  # To store the head of each row
        row_heads[0] = head
        
        # Create the first row and link right pointers
        cur = head
        for j in range(1, n):
            new_node = Node(mat[0][j])
            cur.right = new_node
            cur = new_node
        
        # Create the remaining rows and link both right and down pointers
        for i in range(1, n):
            prev_row = row_heads[i - 1]  # Previous row's head
            cur_row = Node(mat[i][0])    # Current row's head
            row_heads[i] = cur_row       # Save current row head
            prev_row.down = cur_row      # Link down to the first element
            
            cur = cur_row  # Current row traversal
            for j in range(1, n):
                new_node = Node(mat[i][j])
                cur.right = new_node
                prev_row = prev_row.right
                prev_row.down = new_node
                cur = new_node
        
        return head
