from typing import List
from collections import defaultdict
class Solution:
    def matchingCnt(self, n : int, X : List[str]) -> List[int]:
        res,i,chng = [0]*n,0,True
        while chng:
            chng = False
            ind = defaultdict(list)
            for j,s in enumerate(X):
                if i<len(s):
                    chng = True
                    ind[s[i]].append(j)
            for k in ind:
                tot = len(ind[k])
                for j,v in enumerate(ind[k],1): res[v] += tot-j
            i += 1
        return res
