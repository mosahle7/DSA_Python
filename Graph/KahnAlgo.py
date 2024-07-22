from typing import List
from collections import deque

class Solution:
    def isCyclic(self, V: int, adj: List[List[int]]) -> bool:
        indegree = [0] * V
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
                
        q = deque([i for i in range(V) if indegree[i] == 0])
        
        count = 0
        while q:
            cur = q.popleft()
            count += 1
            for neighbor in adj[cur]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        return count != V
