from collections import deque
class Solution:
    def merge(self, root1, root2):
        l=[]
        q=deque()
        q.append(root1)
        while q:
            size=len(q)
            for i in range(size):
                t=q.popleft()
                l.append(t.data)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
        
        q.append(root2)
        while q:
            size=len(q)
            for i in range(size):
                t=q.popleft()
                l.append(t.data)
                if t.left:
                    q.append(t.left)
                if t.right:
                    q.append(t.right)
                    
        l.sort()
        return l


from collections import deque
class Solution:
    def merge(self, root1, root2):
        list1=[]
        list2=[]
        def inOrder(root,l):
            if root:
                inOrder(root.left,l)
                l.append(root.data)
                inOrder(root.right,l)
        inOrder(root1,list1)
        inOrder(root2,list2)
        
        merged_list = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        
        # Append remaining elements from both lists, if any
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1

        return merged_list
