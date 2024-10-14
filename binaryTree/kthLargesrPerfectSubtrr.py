# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        
        def checkPer(root,depth,level=0):
            if root is None: return True
            if root.left is None and root.right is None: return depth==level+1
            if root.left is None or root.right is None: return False

            return checkPer(root.left,depth,level+1) and checkPer(root.right,depth,level+1)

        def calDepth(root):
            depth=0
            while root is not None:
                depth+=1
                root=root.left
            return depth
        
        def fun(root):
            if root is None: return

            depth=calDepth(root)
            if checkPer(root,depth):
                ans.append(depth)
            fun(root.left)
            fun(root.right)
            return
        
        fun(root)
        ans.sort(reverse=True)

        return 2**ans[k-1]-1 if len(ans)>=k else -1


