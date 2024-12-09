class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        m=len(mat)
        n=len(mat[0])

        if tar<mat[0][0] or tar>mat[m-1][n-1]: return False

        low,high=0,m*n-1
            
        while low<=high:
            mid=(low+high)//2
            row=mid//n
            col=mid%n

            if mat[row][col]==tar: return True
            elif mat[row][col]>tar:
                high=mid-1
            else: low=mid+1
        return False





class Solution:
    def searchMatrix(self, mat: List[List[int]], tar: int) -> bool:
        m=len(mat)
        n=len(mat[0])

        if tar<mat[0][0] or tar>mat[m-1][n-1]: return False

        i=0

        def binS(i):
            low,high=0,n-1
            
            while low<=high:
                mid=(low+high)//2

                if mat[i][mid]==tar: return True
                elif mat[i][mid]>tar:
                    high=mid-1
                else: low=mid+1
            return False
