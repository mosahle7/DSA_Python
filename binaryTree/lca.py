
class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        if not root:
            return None
        
        # If either n1 or n2 matches the root's key, return the root
        if root.data == n1 or root.data == n2:
            return root
        
        # Recursively search for LCA in left and right subtrees
        left_lca = self.lca(root.left, n1, n2)
        right_lca = self.lca(root.right, n1, n2)
        
        # If both left_lca and right_lca are not None, then n1 and n2 are on different subtrees
        # and the current root is their LCA
        if left_lca and right_lca:
            return root
        
        # Otherwise, return the non-None node (either left_lca or right_lca)
        return left_lca if left_lca else right_lca
