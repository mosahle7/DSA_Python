
class Solution:
    def getMaxArea(self,hist):
        stack = []
        m=0
        n=len(hist)

        for i,h in enumerate(hist):
            st=i
            while stack and h<stack[-1][1]:
                ind,hei = stack.pop()
                m=max(m,hei*(i-ind))
                st=ind
            stack.append((st,h))

        for i,h in stack:
            m=max(m,(n-i)*h)
        return m
