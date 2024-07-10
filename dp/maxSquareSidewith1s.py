
from typing import List


class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        ma=0
        for i in range(n):
            if ma!=1:
                for j in range(m):
                    if mat[i][j]==1: 
                        ma=1
                        break
        for i in range(n-1):
            for j in range(m-1):
                if mat[i][j]>=1:
                    if mat[i+1][j]>=1 and mat[i][j+1]>=1 and mat[i+1][j+1]>=1:
                        mi=min(mat[i+1][j],mat[i][j+1],mat[i][j])
                        mat[i+1][j+1]=mi+1
                        ma=max(ma,mi+1)
                
        return ma
