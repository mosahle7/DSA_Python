
class Solution:
    def is_sum_tree(self, node):
        def dfs(node):
            if not(node): return 0
            if not(node.left) and not(node.right): return node.data
            
            a=node.data
            l,r=0,0
            l+=dfs(node.left)
            r+=dfs(node.right)
            
            if l==-1 or r==-1 or (l+r)!=a:
                return -1

            return (l+r+a)
        
        c=dfs(node)
        if c==-1: return False
        return True


                
