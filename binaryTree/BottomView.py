from collections import deque, defaultdict

class Solution:
    def bottomView(self, root):
        if not root:
            return []
        
        q = deque([(root, 0)])
        d = defaultdict(int)
        min_hd = max_hd = 0
        
        while q:
            node, hd = q.popleft()
            d[hd] = node.data
            
            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)
            
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        
        # Create the result using the range of horizontal distances
        ans = [d[hd] for hd in range(min_hd, max_hd + 1)]
        return ans
            


class Solution:
    def bottomView(self, root):
        if not root:
            return []
            
        q=deque()
        d=defaultdict()
        
        q.append((root,0))
        
        while q:
            node,hd = q.popleft()
            d[hd]=node.data
            
            if node.left:
                q.append((node.left,hd-1))
            if node.right:
                q.append((node.right,hd+1))
            
        ans=[d[hd] for hd in sorted(d)]
        return ans
            
        
